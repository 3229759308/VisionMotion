# AGENTS.md

## Project

VisionMotion 是一个基于旧 Android 手机摄像头和 Windows PC 的低成本视觉运动测量与机器人实验平台。

## Current Hardware

当前只有：

- Windows PC
- Android 手机

暂时没有：

- 单片机
- 小车
- 电机
- 编码器
- IMU
- 其他比赛硬件

因此现阶段所有功能必须优先使用电脑和手机完成。

## Current Goal

当前最高优先级是完成：

Android Camera  
→ PC  
→ OpenCV  
→ Target Position  
→ World Coordinate  
→ Velocity  
→ Trajectory

在这条基础链路稳定之前，不要主动扩展复杂功能。

## Development Rules

1. 每次只完成一个明确的小任务。
2. 修改前先阅读现有代码和相关文档。
3. 尽量进行小范围修改，不随意重构整个工程。
4. 不随意创建大量文件。
5. 不随意引入新的第三方依赖。
6. 不为了隐藏错误而大量添加 try/except。
7. 关键算法需要解释原理。
8. 每次修改完成后必须给出测试方法。
9. 每个稳定功能完成后应建议进行 Git commit。
10. 不要主动删除 Git 历史。
11. 不要擅自修改已经稳定工作的模块。
12. 参数尽量集中管理，避免大量 magic number。
13. 实验结果尽量保存成可分析的数据。
14. 程序需要考虑以后接入真实机器人，而不只是电脑演示。
15. 如果当前任务可以通过修改现有代码完成，不要为了“工程化”而无意义地增加抽象层。
16. 如果发现当前实现存在明显问题，应先说明问题和修改理由，再进行大范围调整。
17. 当前阶段优先保证可运行、可测试、可理解，再逐步重构。

## Git Workflow

修改代码前优先检查：

- `git status`
- `git diff`

开始新的任务前，应先了解当前工作区是否存在未提交修改。

完成一个独立功能并确认测试通过后，再建议进行 commit。

Commit 应尽量保持单一目的，例如：

- `feat: add camera capture`
- `feat: add realtime fps`
- `fix: handle camera disconnect`
- `docs: update project roadmap`
- `refactor: simplify motion estimator`

前期不要自动替用户执行 Git commit，除非用户明确要求。

不要主动：

- 删除 Git 历史
- 强制覆盖稳定版本
- 执行危险的 reset
- 修改已经提交的历史记录
- 在没有说明风险的情况下执行大范围 Git 操作

如果一次修改风险较大，应先建议创建独立 branch，而不是直接破坏 main。

## Current Restrictions

当前不要主动加入：

- YOLO
- SLAM
- ROS
- Deep Learning
- Complex GUI
- Kalman Filter

除非用户明确要求，或者基础阶段已经完成。

当前优先使用简单、透明、容易理解的方法，例如：

- OpenCV
- HSV
- Threshold
- Contour Detection
- Homography
- Basic Filtering
- CSV Logging
- UDP

不要为了显得高级而优先使用复杂算法。

## AI Collaboration

新的 Codex 会话开始工作前，应优先读取：

1. `AGENTS.md`
2. `README.md`
3. `roadmap.md`
4. `docs/known_issues.md`
5. 最近的 Git 提交记录
6. 当前 `git status`
7. 当前 `git diff`

然后再修改代码。

如果这些文件暂时不存在，不要报错或擅自创建大量替代文件，应先基于已有项目状态继续工作。

如果当前工程状态和文档描述不一致，应先指出差异，不要自行猜测。

如果另一个 Codex 会话已经实现过某个功能，应优先阅读当前代码和 Git 历史，不要重复实现。

不要依赖聊天历史作为唯一上下文来源。

项目中的：

- 文档
- 代码
- Git 历史
- 实验记录

才是主要的长期上下文来源。

## Testing Rules

每次代码修改完成后，应明确告诉用户：

1. 修改了什么。
2. 为什么修改。
3. 如何运行。
4. 如何测试。
5. 正常现象是什么。
6. 如果失败，需要观察什么信息。

不要只说“已经修改完成”。

如果条件允许，应优先进行：

- 最小可运行测试
- 单模块测试
- 输入输出检查
- 基础异常测试

在没有真实硬件的情况下，不要假装已经完成硬件验证。

## Experiment Rules

未来所有重要实验尽量记录：

- 日期
- 实验目的
- 代码版本
- 参数
- 输入条件
- 输出结果
- 问题
- 结论

如果以后进行机器人控制实验，应尽量记录：

- Position
- Velocity
- Target Path
- Actual Path
- Cross Track Error
- Heading Error
- Control Output
- Overshoot
- Settling Time

实验数据尽量保存为：

- CSV
- JSON
- YAML

而不是只保留截图或口头描述。

## Architecture Principle

前期允许使用简单结构快速验证功能。

不要一开始就建立复杂架构。

随着项目逐渐稳定，再逐步拆分为：

- camera
- vision
- calibration
- motion
- filter
- communication
- visualization
- data

每个模块只负责清晰、有限的职责。

## Long-Term Goal

现阶段：

Android Phone  
→ PC  
→ Vision Processing  
→ Motion Measurement  
→ Robot Simulation

以后回到学校后：

Android Phone / Camera  
→ PC Vision  
→ Position / Velocity / Heading  
→ Controller  
→ Communication  
→ MSPM0 / STM32  
→ Motor Driver  
→ Robot  
→ Camera Observation

最终形成：

Observation  
→ Estimation  
→ Control  
→ Motion  
→ Observation

即视觉闭环系统。

## Current Stage

Day 1 - Camera Input 进行中。

Day 0 已完成内容包括：

- Git 配置
- Git repository 初始化
- `.gitignore`
- Python `.venv`
- VS Code Python interpreter
- `README.md`
- `AGENTS.md`
- `roadmap.md`
- 基础 docs
- 第一次 Git commit
- GitHub remote
- 第一次 push

当前已完成 IP Webcam 局域网 HTTP/MJPEG 输入路线的第一轮验证，PC 浏览器和 OpenCV 均可稳定获取实时画面。

HTTP/MJPEG 只是当前已验证的摄像头输入方案之一，尚未确定为最终方案。后续仍计划比较其他摄像头输入方案。

当前继续完成 Day 1 的输入方案比较和验收，不要提前进入目标检测、目标跟踪、标定等后续阶段。
