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

Day 0 已完成并验收，当前准备进入 Day 1 - Camera Input。

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
