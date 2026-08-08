# Architecture

## Current Architecture

当前阶段的系统结构：

Android Phone  
→ Video Stream  
→ Windows PC  
→ OpenCV  
→ Target Detection  
→ Position Estimation  
→ Motion Estimation  
→ Data Logging / Communication

## Current Hardware

当前只有：

- Windows PC
- Android Phone

暂时没有真实机器人硬件。

## Current Responsibilities

### Android Phone

当前主要负责：

- 摄像头采集
- 将视频传输到 PC

后续可能扩展：

- IMU
- GPS
- Microphone
- 其他 Android 传感器

### Windows PC

PC 当前和后续主要负责：

- 视频获取
- OpenCV 图像处理
- 目标检测
- 坐标转换
- 运动状态计算
- 数据记录
- 数据可视化
- 通信
- 机器人控制算法
- 仿真

## Planned Data Flow

第一阶段：

Android Camera  
→ PC  
→ Pixel Coordinate `(u, v)`

之后：

Pixel Coordinate `(u, v)`  
→ Calibration / Homography  
→ World Coordinate `(x, y)`

之后：

World Coordinate `(x, y)`  
→ Motion Estimation  
→ Velocity / Trajectory

再之后：

Motion State  
→ UDP  
→ Robot Simulation

回学校后：

Motion State  
→ Controller  
→ Communication  
→ MSPM0 / STM32  
→ Motor Driver  
→ Robot

## Architecture Principle

当前阶段遵循：

1. 先验证功能，再进行模块拆分。
2. 不提前建立复杂架构。
3. 每个模块只承担清晰职责。
4. 视觉算法与具体通信方式尽量解耦。
5. 运动测量与机器人控制尽量解耦。
6. 实验数据能够独立保存和分析。
7. 后续真实机器人应尽量能够替换当前模拟机器人，而不需要重写整个视觉系统。

## Future Modules

功能稳定以后，可能逐步拆分为：

- `camera`
- `vision`
- `calibration`
- `motion`
- `filter`
- `communication`
- `visualization`
- `data`

这些只是未来规划。

当前不要为了符合该结构而提前创建大量目录。

## Long-Term Closed Loop

最终目标：

Camera Observation  
→ Vision Measurement  
→ State Estimation  
→ Controller  
→ Robot Motion  
→ Camera Observation

形成完整的视觉反馈闭环。