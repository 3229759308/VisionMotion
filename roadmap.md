# VisionMotion Roadmap

## Day 0 - Engineering Setup

- [x] 安装并确认 Git
- [x] 配置 Git 用户名
- [x] 配置 Git 隐私邮箱
- [x] 配置 Windows Git 换行处理
- [x] 创建 VisionMotion 项目目录
- [x] 使用 VS Code 打开并信任项目
- [x] 初始化本地 Git 仓库
- [x] 创建 `.gitignore`
- [x] 创建 Python `.venv`
- [x] 配置 VS Code Python Interpreter
- [x] 创建 `README.md`
- [x] 创建 `AGENTS.md`
- [x] 创建 `roadmap.md`
- [x] 创建基础 `docs/`
- [x] 创建 `requirements.txt`
- [x] 完成第一次 Git commit
- [x] 创建 GitHub 私有仓库
- [x] 连接 GitHub remote
- [x] 完成第一次 push
- [x] Day 0 最终验收

---

## Day 1 - Camera Input

目标：

让旧 Android 手机摄像头能够稳定向 PC 提供实时视频，并由 OpenCV 获取。

任务：

- [x] 完成 HTTP/MJPEG 视频传输方案第一轮验证
- [x] 完成 DroidCam USB + ADB Forward 视频传输方案第一轮验证
- [x] 整理并比较已验证的摄像头输入方案，确定最终方案
  - 主方案：DroidCam USB + ADB Forward
  - 备用方案：IP Webcam / Wi-Fi MJPEG
- [x] PC 能获取手机实时画面
- [x] OpenCV 成功读取视频流
- [x] 在画面中显示原始分辨率（已确认原始帧为 1920×1080）
- [x] 实时计算 FPS
- [x] 检查画面延迟
- [x] 检查掉帧情况
- [x] 完成约 10 分钟稳定性测试

验收标准：

- 视频能够稳定运行
- OpenCV 可以连续读取画面
- 能够显示分辨率和 FPS
- 暂时不进行目标识别

---

## Day 2 - Basic Target Detection

目标：

使用简单、透明的传统视觉方法识别彩色目标。

状态：进行中。第一版受控环境基础检测器已完成代码 checkpoint，仍需完成边界验证与阶段收尾。

任务：

- [x] BGR → HSV
- [x] HSV 阈值分割
- [x] 二值图
- [x] 形态学处理
- [x] 轮廓检测
- [x] 选择有效目标
- [x] 计算目标中心 `(u, v)`
- [x] 在画面上显示目标位置

收尾任务：

- [x] 完成无目标场景测试，确认无有效候选时 `Target Detected: False`
- [x] 测试更大同色干扰物场景，记录最大轮廓策略的误检边界
- [ ] 补充更大光照变化和距离变化测试，记录固定 HSV 与面积门槛的适用范围
- [ ] 完成 Day 2 最终验收与阶段收尾

当前实现说明：

- 代码 checkpoint：`6a29d16 feat: add basic color target detection`
- 当前实现是第一版受控环境基础检测器，不是最终鲁棒目标识别方案
- 已知限制包括固定 HSV 阈值、最大轮廓策略、固定面积门槛，以及遮挡对面积和视觉质心的影响

暂时不使用：

- YOLO
- Deep Learning

---

## Day 3 - Target Tracking

目标：

记录目标随时间的运动轨迹。

任务：

- [ ] 保存历史中心点
- [ ] 绘制运动轨迹
- [ ] 限制轨迹长度
- [ ] 处理短暂目标丢失
- [ ] 处理错误轮廓

---

## Day 4-5 - Calibration

目标：

把像素坐标转换成真实世界坐标。

任务：

- [ ] 建立平面坐标系
- [ ] 获取四个参考点
- [ ] 学习 Homography
- [ ] 计算单应矩阵
- [ ] Pixel → World Coordinate
- [ ] 输出 `(x, y)`，单位 mm
- [ ] 测量定位误差

目标精度：

第一阶段约 ±5~10 mm。

---

## Day 6 - Motion Estimation

目标：

从连续位置数据计算运动状态。

任务：

- [ ] 使用真实 timestamp
- [ ] 计算 `dt`
- [ ] 计算 `vx`
- [ ] 计算 `vy`
- [ ] 计算速度 `v`
- [ ] 分析速度噪声

---

## Day 7 - Data Logging

目标：

建立可重复分析的实验记录。

任务：

- [ ] CSV 数据记录
- [ ] timestamp
- [ ] x
- [ ] y
- [ ] vx
- [ ] vy
- [ ] velocity
- [ ] XY 轨迹绘图
- [ ] Velocity-Time 曲线

---

## Day 8 - Filtering

目标：

理解并比较基础滤波算法。

顺序：

- [ ] Raw Data
- [ ] Moving Average
- [ ] EMA / Low Pass
- [ ] 比较噪声
- [ ] 比较延迟

基础工作完成之前暂不使用 Kalman Filter。

---

## Day 9-10 - Engineering Refactor

目标：

在已有功能稳定以后逐步整理工程结构。

可能逐步拆分：

- camera
- vision
- calibration
- motion
- filter
- visualization
- data

原则：

先验证，再重构。

---

## Day 11 - Communication

目标：

建立独立于具体机器人硬件的数据通信层。

任务：

- [ ] UDP Sender
- [ ] UDP Receiver
- [ ] JSON 数据协议
- [ ] PC 本地通信测试

以后可扩展：

- Serial
- Bluetooth
- Wi-Fi

---

## Day 12-14 - Robot Simulation

目标：

在没有真实小车的情况下建立机器人闭环实验。

任务：

- [ ] 建立简单二维机器人模型
- [ ] 学习 Pure Pursuit
- [ ] 学习 Stanley Controller
- [ ] 学习 A*
- [ ] 路径生成
- [ ] 路径跟踪
- [ ] 闭环仿真

---

## Back to School

以后有真实硬件后：

Vision  
→ Position / Velocity / Heading  
→ Controller  
→ Communication  
→ MSPM0 / STM32  
→ Motor Driver  
→ Robot  
→ Vision

最终目标：

建立可测量、可记录、可重复、可让 AI 分析的机器人闭环实验平台。
