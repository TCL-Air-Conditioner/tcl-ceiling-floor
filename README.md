# TCL Ceiling & Floor 视频网页

本仓库以 [VoxIN EVO T4](https://github.com/TCL-Air-Conditioner/voxin-evo-t4) 的页面和构建代码为模板，包含 12 个视频页面。如果某条 MP4 尚未提供，该页面会显示 `Video coming soon.`；这是视频占位，不代表视频已经上传。

## 上传视频

将每条 MP4 放到下表对应路径，保持文件名一致。提交后，GitHub Actions 会构建网站、生成视频封面并发布。启用部署时，需要在仓库 Settings → Pages 中将 Source 设为 GitHub Actions。不要用其他产品的视频代替。

为兼容更多浏览器，构建时会将非 H.264 视频转换为高质量 H.264 播放副本；H.264 视频保持原样。仓库中的原始视频不会被修改，网页发布的是播放副本。

| 序号 | 视频名称 | MP4 文件路径 |
|---|---|---|
| 1 | Filter Removal | `filter-removal/filter-removal.mp4` |
| 2 | Filter Installation | `filter-installation/filter-installation.mp4` |
| 3 | Easy Maintenance PCB | `easy-maintenance-pcb/easy-maintenance-pcb.mp4` |
| 4 | Fan Motor Maintenance | `fan-motor-maintenance/fan-motor-maintenance.mp4` |
| 5 | 130° Wide Airflow | `130-wide-airflow/130-wide-airflow.mp4` |
| 6 | App Connection | `app-connection/app-connection.mp4` |
| 7 | Vertical Swing | `vertical-swing/vertical-swing.mp4` |
| 8 | Smart Energy Saving | `smart-energy-saving/smart-energy-saving.mp4` |
| 9 | Electricity Consumption Visualization | `electricity-consumption-visualization/electricity-consumption-visualization.mp4` |
| 10 | Self-Cleaning | `self-cleaning/self-cleaning.mp4` |
| 11 | Sleep Mode | `sleep-mode/sleep-mode.mp4` |
| 12 | GEN Mode | `gen-mode/gen-mode.mp4` |

## 本地预览

安装 Python 3；已有 MP4 时还需安装 FFmpeg。运行 `python3 build_pages.py /tmp/tcl-ceiling-floor-site`，目标目录须不存在或为空，然后用静态网页服务器打开输出目录。

## 模板来源

基于 `TCL-Air-Conditioner/voxin-evo-t4` 提交 `43b16ac4582c9f8fd0a969a1ca38f0716b30a613`。保留原有播放器及缓存逻辑，仅替换产品名称、12 个页面名称和文件路径。
