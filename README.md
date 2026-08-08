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

Day 1 - Camera Input 进行中。

使用 IP Webcam 通过局域网 HTTP/MJPEG 提供视频的路线已完成第一轮验证，PC 浏览器和 OpenCV 均可稳定获取实时画面。该路线目前尚未确定为最终摄像头输入方案。

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
