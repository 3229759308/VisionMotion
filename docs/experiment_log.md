# Experiment Log

用于记录项目中的重要实验、参数和结果。

建议每次重要实验都记录：

- 实验编号
- 日期
- 实验目的
- 当前代码版本
- 实验条件
- 参数
- 测试方法
- 结果
- 问题
- 结论
- 下一步

---

## EXP-000

### Date

2026-08-08

### Purpose

建立 VisionMotion 项目的基础开发环境和版本管理结构。

### Environment

- Windows
- Python 3.12
- VS Code
- Git
- Android Phone

### Completed

- Git 全局配置
- Git 仓库初始化
- `.gitignore`
- Python `.venv`
- VS Code Python Interpreter
- `README.md`
- `AGENTS.md`
- `roadmap.md`
- 基础 `docs`

### Result

Day 0 基础工程环境正在搭建中。

### Conclusion

工程地基基本完成，接下来继续完成：

- `requirements.txt`
- 第一次 Git commit
- GitHub 私有仓库
- remote
- 第一次 push

### Final Status

Day 0 已完成并通过最终验收：

- `requirements.txt` 已创建
- 第一次 Git commit 已完成
- GitHub remote 已配置
- 第一次 push 已完成
- 最终 Git 工作区 clean
- `main` 与 `origin/main` 同步

### Next Stage

下一阶段为 Day 1 - Camera Input，当前尚未开始。

---

## EXP-001

### Date

2026-08-08

### Purpose

验证 Android 手机通过局域网 HTTP/MJPEG 向 Windows PC 提供实时视频，并由 OpenCV 连续读取和显示的可行性与基础性能。

### Environment

- Windows PC
- Android 13 手机
- IP Webcam
- Python 3.12 项目 `.venv`
- `numpy==2.5.1`
- `opencv-python==5.0.0.93`
- 开发分支：`feat/camera-input`
- 实验代码：`camera_test.py`

### Video Input

- 视频地址形式：`http://<phone-ip>:8080/video`
- 本次测试地址：`http://192.168.2.201:8080/video`
- 传输方式：局域网 HTTP/MJPEG

### Test Method

- 先在 PC 浏览器中打开视频地址，确认可以稳定观看实时画面。
- 使用 `cv2.VideoCapture()` 打开视频流，检查 `cap.isOpened()` 和 `cap.read()`。
- 连续读取并显示画面，使用 1 秒统计窗口测量实际读取 FPS。
- 观察画面延迟、卡顿、断流和约 10 分钟运行稳定性。
- 按 `q` 退出，并确认程序释放视频流和销毁 OpenCV 窗口。

### Result

- PC 浏览器可以稳定观看视频流。
- `cv2.VideoCapture()` 成功打开视频流，`cap.isOpened()` 返回 `True`。
- `cap.read()` 可以持续取得有效 frame。
- 原始 `frame.shape` 为 `(1080, 1920, 3)`，即 1920×1080 BGR 图像。
- 实际读取 FPS 基本稳定在约 30 FPS，画面左上角显示绿色 FPS 信息。
- 实际观察延迟小于约 0.5 s。
- 约 10 分钟测试期间视频稳定，几乎无明显卡顿或断流。
- 960×540 resize 仅用于显示，不代表输入视频的原始分辨率。
- 按 `q` 可以正常退出；退出时执行 `cap.release()` 和 `cv2.destroyAllWindows()`。

### Conclusion

HTTP/MJPEG Camera Input 当前验证成功，可以作为 VisionMotion 的可用摄像头输入方案。该方案尚未确定为最终方案，后续仍需与其他摄像头输入方式进行比较。

### Next Action

继续完成 Day 1 的摄像头输入方案比较和剩余验收，不提前进入目标检测、跟踪或标定阶段。
## EXP-002
### DroidCam USB / ADB Camera Input

### Test Method

- Android 手机开启 USB 调试，并运行 DroidCam App。
- 使用 DroidCam Windows Client 验证 USB 连接和实时视频输出。
- 使用 OpenCV 分别测试默认摄像头索引、DirectShow 和 Media Foundation 后端。
- 使用 ADB 建立端口转发：`tcp:4747 -> tcp:4747`。
- 关闭 DroidCam Client 中占用手机的视频 Source，通过 `http://127.0.0.1:4747/video` 直接访问 DroidCam 视频流。
- 使用 OpenCV `cv2.VideoCapture()` 读取经 ADB USB 转发的视频流。
- 分别测试默认 1280×720 视频流和显式指定的 1920×1080 视频流。
- 使用 1 秒统计窗口测量实际 OpenCV 读取 FPS，并进行约 5 分钟稳定性测试。
- 改变环境亮度，观察自动曝光对实际 FPS 的影响。

### Result

- DroidCam Windows Client 可以通过 USB 正常连接手机，并稳定显示实时画面。
- Windows 相机应用可以正常读取 `DroidCam Video` 虚拟摄像头。
- OpenCV 通过虚拟摄像头索引读取时存在兼容问题：
  - 默认方式可打开设备，但得到 `Start DroidCam` 占位画面。
  - DirectShow (`CAP_DSHOW`) 无法正常打开该设备。
  - Media Foundation (`CAP_MSMF`) 可以读取帧，但仍得到占位画面。
- ADB 可以正常识别手机，设备状态为 `device`。
- 使用 ADB `forward tcp:4747 tcp:4747` 可以通过 USB 建立 DroidCam HTTP 视频通道。
- DroidCam Client Source 开启时，`/video` 会显示 Busy/Unavailable；关闭该 Source 后可以正常访问视频流。
- OpenCV 可以成功读取 `http://127.0.0.1:4747/video`。
- 默认 `/video` 输出为 `(720, 1280, 3)`，即 1280×720 BGR 图像。
- 使用 `/video/1920x1080` 后，输出为 `(1080, 1920, 3)`，即 1920×1080 BGR 图像。
- 1920×1080 条件下，在光线充足且相机静止时，OpenCV 实际读取 FPS 基本稳定在 30 FPS。
- 连续约 5 分钟运行无断流、无明显卡顿，整体稳定。
- DroidCam Target FPS 设置为 30，AE FPS Range 显示为 5–30。
- 实测环境亮度会明显影响实际 FPS：
  - 光线充足时约 30 FPS；
  - 稍暗时约 25 FPS；
  - 更暗时约 20 FPS。
- 主观观察 USB DroidCam 方案延迟较小，画面质量优于此前测试的 IP Webcam / MJPEG 方案。

### Conclusion

DroidCam + USB + ADB Forward 方案验证成功。当前环境下可以稳定向 OpenCV 提供 1920×1080、最高约 30 FPS 的实时视频输入，并绕过 DroidCam Windows 虚拟摄像头与 OpenCV 的兼容问题。

实验表明，当前帧率变化主要受到手机摄像头自动曝光和环境照明影响，而不是 720p 或 USB 带宽本身限制。

综合与 IP Webcam / Wi-Fi MJPEG 方案的对比结果，当前确定 DroidCam USB + ADB Forward 为 VisionMotion 的主摄像头输入方案，IP Webcam / Wi-Fi MJPEG 作为备用方案。
### Next Action

完成 Day 1 收尾和 Git checkpoint，之后再进入下一阶段。当前不提前进入目标检测、跟踪或标定。
