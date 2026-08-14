# VisionMotion

基于旧 Android 手机和 Windows PC 的低成本视觉运动测量与机器人实验平台。

## Project Goal

当前阶段使用：

- Windows PC
- Android 手机

目标是逐步实现：

Android Camera  
→ PC Video Capture  
→ OpenCV  
→ Target Detection  
→ World Coordinate  
→ Motion Estimation  
→ Data Logging  
→ Communication  
→ Robot Simulation

后续回到学校后，再接入 MSPM0 / STM32 和真实小车，形成视觉反馈闭环。

## Current Stage

Day 2 - Basic Target Detection 已完成。

Day 3 - Target Tracking 尚未开始。

当前分支为 `feat/basic-target-detection`，已完成第一个代码 checkpoint：
`6a29d16 feat: add basic color target detection`。

当前摄像头输入方案：

- 主方案：DroidCam + USB + ADB Forward
- 备用方案：IP Webcam / Wi-Fi MJPEG

主方案已验证 OpenCV 可稳定读取 1920×1080 视频，在正常光照下约 30 FPS，并通过连续约 5 分钟稳定性测试。

当前已使用 HSV 阈值分割、形态学闭运算和外部轮廓检测，实现橙色目标候选选择、面积门槛、轮廓质心、Bounding Box 与实时位置显示。

这只是面向受控环境的第一版基础检测器。实验已确认：更大同色物体会被最大轮廓策略误选；固定 HSV 阈值只在有限光照范围内有效；强烈过曝会丢失局部颜色信息；固定面积门槛会拒绝像素面积过小的远距离真实目标；遮挡会改变轮廓面积和视觉质心。因此当前实现不能视为最终鲁棒目标识别方案，也尚未实现 Tracking。

## Environment

- Windows
- Python 3.12
- VS Code
- Git
- Android Phone

## Development Principle

先完成基础链路，再逐步增加复杂功能。

当前暂不优先加入：

- YOLO
- SLAM
- ROS
- Deep Learning
- Complex GUI
