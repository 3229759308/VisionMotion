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

Day 2 - Basic Target Detection 准备开始，尚未进入实现。

当前摄像头输入方案：

- 主方案：DroidCam + USB + ADB Forward
- 备用方案：IP Webcam / Wi-Fi MJPEG

主方案已验证 OpenCV 可稳定读取 1920×1080 视频，在正常光照下约 30 FPS，并通过连续约 5 分钟稳定性测试。

下一阶段为 Day 2 - Basic Target Detection，目标是使用简单、透明的传统视觉方法识别彩色目标。

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
