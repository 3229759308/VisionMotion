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

---

## EXP-003

### Date

2026-08-11（2026-08-14 完成边界验证与最终验收）

### Title

Day 2 - Basic Color Target Detection

### Purpose

在 DroidCam USB + ADB Forward 已稳定提供视频输入的基础上，使用简单、透明的传统视觉方法建立并验证第一版橙色目标检测流程，输出目标是否有效、像素中心和轮廓面积。

### Version

- 开发分支：`feat/basic-target-detection`
- 代码 checkpoint：`6a29d16 feat: add basic color target detection`
- 实验代码：`target_detection_test.py`
- checkpoint 后初始工作区状态：clean

### Environment and Input

- Windows PC
- Android 手机
- DroidCam USB + ADB Forward
- OpenCV 视频地址：`http://127.0.0.1:4747/video/1920x1080`
- 输入分辨率：1920×1080
- 正常光照下实际读取帧率：约 30 FPS
- 受控实验目标：橙色物体
- 主要背景：大理石桌面

### Color Sampling

- 大理石桌面典型 BGR：约 `[179, 184, 187]`
- 橙色目标典型 BGR：约 `[15, 106, 208]`
- 橙色目标典型 HSV：约 `[14, 237, 208]`
- 暗光下同一橙色目标 HSV：曾测得约 `[11, 193, 152]`
- 实验观察：色相 `H` 相对稳定，明度 `V` 会随环境亮度明显变化

### Parameters and Method

- 将摄像头 BGR 帧转换为 HSV。
- 根据实测颜色建立第一版橙色阈值：
  - `lower_orange = (8, 150, 120)`
  - `upper_orange = (20, 255, 255)`
- 使用 `cv2.inRange()` 生成二值 Mask。
- 使用 5×5 椭圆结构元素执行 `MORPH_CLOSE` 闭运算，减少目标区域内的小孔洞和裂缝。
- 使用 `findContours()`、`RETR_EXTERNAL` 和 `CHAIN_APPROX_SIMPLE` 提取外部轮廓。
- 将面积最大的外部轮廓作为 candidate，并设置 `MIN_TARGET_AREA = 5000`；仅当 `candidate_area >= 5000` 时将其升级为 target。
- 使用 `cv2.moments()` 计算目标轮廓质心；当 `m00 == 0` 时，代码回退到外接矩形中心。
- 在画面上显示绿色 Bounding Box、蓝色目标中心点和 `Target: (x, y)`；终端周期性输出检测状态、中心、面积、轮廓数量和候选面积。

### Test Method

- 在正常光照下放置完整橙色目标，观察二值 Mask、外部轮廓、检测状态、中心坐标和面积。
- 完全移除橙色目标，检查无候选轮廓时的轮廓数量和检测状态。
- 将橙色目标缩小到轮廓面积低于门槛，检查“存在轮廓”和“有效目标”是否被正确区分。
- 将目标从画面左侧移动到右侧，检查 `target_x` 是否随实际运动单调增大。
- 比较 `cv2.moments()` 轮廓质心与外接矩形中心，记录完整目标和遮挡目标的中心差值。
- 遮挡目标，观察轮廓面积、碎片轮廓数量和视觉质心变化。
- 同时保留真实橙色目标并加入面积更大的橙色手机屏幕区域，在不修改代码和参数的条件下观察最大轮廓策略的选择结果。
- 保持 HSV 阈值不变，逐步改变目标表面的光照，记录中心采样值、轮廓数量、检测状态和暗光 FPS；另用强光直射验证过曝影响。
- 保持目标、光照、HSV 阈值、面积门槛和代码不变，只改变目标到摄像头的距离，对比轮廓面积位于 `MIN_TARGET_AREA = 5000` 两侧时的检测结果。

### Results

- DroidCam USB + ADB Forward 继续稳定向 OpenCV 提供 1920×1080 视频；正常光照下约 30 FPS。
- 在当前受控场景中，真实目标轮廓面积通常约 80000 px²，大量噪声轮廓仅为 0 到几十 px²。
- 完全移除橙色目标时，输出 `Contours: 0` 和 `Target Detected: False`。
- 正常目标面积约 80000 px² 时，输出 `Target Detected: True`。
- 小目标面积约 2800 px² 时仍可观察到 `Contours > 0`，但因未达到 5000 px² 门槛，输出 `Target Detected: False`。
- 目标从左向右移动时，`target_x` 实测约为 `271 → 330 → 697 → 1137 → 1565`，变化方向符合预期。
- 完整近似圆形目标的轮廓质心与外接矩形中心差值通常约为 `(-2, -1)` px。
- 遮挡后中心差值增大到约 7～8 px，说明视觉质心会随可见轮廓形状变化。
- 遮挡实验中目标面积由约 82000 px² 降至约 24000～34000 px²，并出现更多碎片轮廓。
- 已实现并实际观察到绿色 Bounding Box、蓝色目标中心点、`Target Detected: True / False`、实时 `Target Center (x, y)`、`Target Area` 和画面中的 `Target: (x, y)`。
- 同色干扰物实验中，真实橙色圆形目标面积约为 `82495.0 px²`，左侧橙色手机屏幕区域面积约为 `617084.5 px²`。
- 最大轮廓策略最终选择了面积更大的手机橙色屏幕，绿色 Bounding Box 随之转移；对应输出为 `Target Center: (511, 615)`、`Target Area: 617084.5`，候选面积包含 `[617084.5, 82495.0, 63.0, 2.0, 1.5]`。
- 该结果符合 `max(contours, key=cv2.contourArea)` 的当前规则，验证了“最大同色轮廓不能可靠代表目标身份”的失效边界，不是 OpenCV 或程序运行错误。
- 正常光线亮面中心采样为 `BGR [19, 82, 208]`、`HSV [10, 232, 208]`，处于当前阈值范围内；同一目标阴影面为 `BGR [6, 35, 138]`、`HSV [7, 244, 138]`，其中 `H = 7` 已低于下限 8。
- 较暗环境中心采样为 `BGR [25, 51, 121]`、`HSV [8, 202, 121]`，其中 `H = 8`、`V = 121` 已接近阈值下边界。继续降低亮度后，代表采样依次为 `BGR [9, 19, 52] / HSV [7, 211, 52]`、`BGR [11, 17, 50] / HSV [5, 199, 50]` 和 `BGR [11, 17, 40] / HSV [6, 185, 40]`，均出现 `Contours: 0`、`Target Detected: False`。
- 暗光失效时 FPS 降至约 `14.21～14.27`，与此前观察到的手机自动曝光导致帧率下降现象一致。
- 强光直射亮面时中心采样为 `BGR [253, 255, 255]`、`HSV [30, 2, 255]`；像素接近白色且 `S = 2`，说明强烈过曝会使局部橙色色彩信息丢失。
- 距离实验的较远状态仍存在轮廓：`Contours: 5`、`Areas: [4531.5, 0.0, 0.0, 0.0, 0.0]`，但最大面积 `4531.5 < 5000`，因此 `Target Detected: False`。
- 同一目标稍微靠近后，面积增至 `5183.5 > 5000`，输出 `Target Detected: True`、`Target Center: (779, 555)`、`Box Center: (781, 557)`、`Delta: (-2, -2)`。
- 两类失败已经明确区分：暗光时目标像素越出固定 HSV 范围，Mask 中目标消失并导致 `Contours = 0`；远距离时轮廓仍存在，但因 `Area < 5000` 被固定面积门槛拒绝。距离实验不以画面中心 HSV 采样作为主要依据，因为目标未必位于图像中心。

### Known Limitations

- 固定 HSV 阈值已确认只在有限光照范围内有效：暗光会使 `H / V` 越界并使目标轮廓消失，强烈过曝会降低饱和度并丢失颜色信息。HSV 相比直接 BGR 仍更适合当前颜色分割。
- 最大轮廓策略已在更大同色干扰物实验中确认会选错目标，不能将最大同色轮廓等同于目标身份。
- 固定 `MIN_TARGET_AREA = 5000` 已确认存在距离 / 图像尺度边界：远距离真实目标即使仍有轮廓，也可能因像素面积低于门槛而被拒绝。
- 遮挡会降低轮廓面积、增加碎片轮廓，并改变视觉质心。
- 当前规则是教学和基础实验阶段的简化假设，只能称为“第一版受控环境基础检测器”，不能视为最终鲁棒目标识别方案。

### Conclusion

Day 2 的基础检测链路已经打通：`BGR → HSV → 阈值分割 → 二值 Mask → 闭运算 → 外部轮廓 → 面积门槛 → 轮廓质心与画面标注`。在当前受控环境中，橙色目标可以被稳定区分，并能输出方向正确的像素中心位置。

Day 2 已完成最终验收与阶段收尾。当前成果定位为“第一版受控环境基础检测器”：基础检测链路可运行、可观察、可解释，同时已实际验证更大同色干扰物、固定 HSV 光照边界、强光过曝、固定面积门槛距离边界和遮挡影响。它不是鲁棒目标识别系统，尚未解决目标身份判断，也不能适应任意光照或距离。

下一阶段为 Day 3 - Target Tracking，但尚未开始实现。开始前先理解单帧目标检测与连续目标跟踪的区别，以及保存历史中心点的必要性；暂不进入 Calibration / Homography、Motion Estimation、Kalman Filter 或 YOLO / Deep Learning。
