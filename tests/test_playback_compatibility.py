import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from build_pages import prepare_playback_video

@unittest.skipUnless(shutil.which('ffmpeg'), 'ffmpeg is required')
class PlaybackCompatibilityTests(unittest.TestCase):
    def test_hevc_is_published_as_h264_without_modifying_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);source=root/'original.mp4';target=root/'output.mp4'
            subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','lavfi','-i','color=c=red:s=64x64:r=10','-t','1','-c:v','libx265','-x265-params','pools=1:frame-threads=1:log-level=error','-pix_fmt','yuv420p',str(source)],check=True,capture_output=True)
            original=source.read_bytes()
            prepare_playback_video(source,target)
            self.assertEqual(source.read_bytes(),original)
            inspection=subprocess.run(['ffmpeg','-hide_banner','-i',str(target)],capture_output=True,text=True)
            self.assertIn('Video: h264',inspection.stderr)
            self.assertGreater(target.stat().st_size,0)
            data=target.read_bytes();self.assertLess(data.find(b'moov'),data.find(b'mdat'))

    def test_h264_is_copied_without_reencoding(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);source=root/'original.mp4';target=root/'output.mp4'
            subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','lavfi','-i','color=c=blue:s=64x64:r=10','-t','1','-c:v','libx264','-pix_fmt','yuv420p',str(source)],check=True,capture_output=True)
            prepare_playback_video(source,target)
            self.assertEqual(source.read_bytes(),target.read_bytes())
