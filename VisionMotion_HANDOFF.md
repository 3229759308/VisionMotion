# VisionMotion HANDOFF

> 用途：当 ChatGPT / Codex 对话过长、需要新开对话时，用这份文件快速恢复项目上下文。
> 当前整理日期：2026-08-14

---

## 1. 项目概况

项目名：`VisionMotion`

项目路径：

```text
D:\AAAprojects\VisionMotion
```

长期目标：

```text
Camera Observation
→ Target Detection
→ World Coordinates
→ Motion Estimation
→ Control
→ Robot Motion
→ Re-observation
```

最终希望建立一个可测量、可记录、可重复、可让 AI 分析的机器人视觉闭环实验平台。

当前原则：先使用传统、透明、可解释的计算机视觉方法，不提前进入复杂 AI 方案。

---

## 2. 当前开发状态

当前阶段：

```text
Day 2 - Basic Target Detection
```

当前分支：

```text
feat/basic-target-detection
```

代码 checkpoint：

```text
6a29d16 feat: add basic color target detection
```

文档 checkpoint：

```text
c0cf845c53879f88108d4d2155f821e8b5648d1d
```

当前 Git 状态：

```text
working tree clean
local / remote synchronized
upstream: origin/feat/basic-target-detection
```

Day 2 尚未完成。

---

## 3. 已完成阶段

### Day 0 - Engineering Setup

已完成 Git、GitHub 私有仓库、`.gitignore`、`.venv`、VS Code Python Interpreter、README、AGENTS、roadmap、docs、requirements 和基础 commit / push 流程。

### Day 1 - Camera Input

主方案：

```text
DroidCam + USB + ADB Forward
```

ADB 路径：

```text
D:\scrcpy\scrcpy-win64-v3.3.3\adb.exe
```

常用转发命令：

```powershell
& "D:\scrcpy\scrcpy-win64-v3.3.3\adb.exe" forward tcp:4747 tcp:4747
```

OpenCV 当前视频地址：

```text
http://127.0.0.1:4747/video/1920x1080
```

验证结果：

- 1920×1080
- 正常光照下约 30 FPS
- 5 分钟以上稳定运行
- 延迟较低
- 主观画质优于 Wi-Fi MJPEG

注意：

- ADB Forward 是运行时状态，电脑重启 / ADB 重置 / 手机重连后可能需要重新执行。
- DroidCam Windows Client Source 打开时可能占用视频源，使 `/video` 显示 Busy / Unavailable。

备用方案：

```text
IP Webcam / Wi-Fi MJPEG
```

曾使用：

```text
http://192.168.2.201:8080/video
```

验证结果：

- 1920×1080
- 约 30 FPS
- 约 10 分钟稳定
- 延迟主观 < 0.5 s

---

## 4. Python 环境

全局 Python：

```text
D:\Python\python.exe
Python 3.12.7
```

项目虚拟环境：

```text
D:\AAAprojects\VisionMotion\.venv\Scripts\python.exe
```

PowerShell 激活：

```powershell
.\.venv\Scripts\Activate.ps1
```

VS Code Python 扩展目前可能自动激活 `.venv`。

主要依赖：

```text
numpy==2.5.1
opencv-python==5.0.0.93
```

推荐使用：

```powershell
python -m pip ...
```

---

## 5. 当前 Day 2 代码

主要实验文件：

```text
target_detection_test.py
```

当前处理链路：

```text
Camera Frame
→ BGR
→ HSV
→ HSV Threshold
→ Binary Mask
→ Morphological Closing
→ External Contours
→ Largest Candidate
→ Area Gate
→ Target
→ Bounding Box
→ Moments Centroid
→ Visualization / Console Output
```

---

## 6. 当前颜色检测参数

第一版橙色 HSV 阈值：

```python
lower_orange = (8, 150, 120)
upper_orange = (20, 255, 255)
```

面积门槛：

```python
MIN_TARGET_AREA = 5000
```

当前候选选择：

```python
candidate = max(contours, key=cv2.contourArea)
```

含义：

```text
最大的橙色外轮廓 = candidate
candidate_area >= 5000
→ target
```

这只是教学阶段的简化规则，不代表最终目标身份判定方法。

---

## 7. 已学习并实际验证的视觉知识

已经完成并理解：

- `frame.shape = (height, width, channels)`
- 像素索引 `frame[y, x]`
- OpenCV 默认颜色顺序 BGR
- BGR → HSV
- OpenCV HSV：H 约 0–179，S/V 0–255
- `cv2.inRange()`
- 二值 Mask
- Morphological Closing
- 5×5 椭圆结构元素
- `cv2.findContours()`
- `cv2.RETR_EXTERNAL`
- `cv2.CHAIN_APPROX_SIMPLE`
- `cv2.contourArea()`
- 最大轮廓 candidate
- 面积门槛
- `cv2.boundingRect()`
- Bounding Box 中心
- `cv2.moments()`
- `m00 / m10 / m01`
- 轮廓质心 `x=m10/m00, y=m01/m00`
- `m00 == 0` 时回退到 Bounding Box 中心
- 原始图像坐标：左上角 `(0,0)`，x 向右，y 向下
- 原始 1920×1080 与显示缩放 960×540 的坐标不能混用
- Python 缩进相当于 C/C++ 中的作用域 / 花括号

---

## 8. Day 2 实测数据

### BGR / HSV 采样

大理石桌面：

```text
BGR ≈ [179, 184, 187]
```

橙色目标典型：

```text
BGR ≈ [15, 106, 208]
HSV ≈ [14, 237, 208]
```

暗光橙色：

```text
BGR ≈ [37, 78, 152]
HSV ≈ [11, 193, 152]
```

实验结论：

- H 相对稳定
- V 会随亮度明显下降
- S 也会变化
- HSV 比直接使用 BGR 更适合当前颜色分割，但并不等于不受光照影响

---

## 9. Mask / Morphology 实验

当前流程：

```python
mask = cv2.inRange(hsv_frame, lower_orange, upper_orange)
```

随后使用：

```text
5×5 ellipse kernel + MORPH_CLOSE
```

作用：

- 减少小孔洞
- 减少小裂缝
- 不强行填满所有大孔洞

当前目标主要依赖外部轮廓，因此没有继续过度形态学处理。

---

## 10. Contour / Area 实验

当前受控环境中，完整真实目标面积通常约：

```text
80,000 px²
```

部分实验约：

```text
81,000 ~ 87,000 px²
```

大量小噪声：

```text
0 ~ 几十 px²
```

面积门槛：

```text
MIN_TARGET_AREA = 5000
```

验证：

正常目标：

```text
Area ≈ 80,000
→ Target Detected: True
```

小目标 / 小候选：

```text
Contours > 0
Area ≈ 2,800
→ Target Detected: False
```

说明：

```text
candidate 存在
≠
candidate 一定是有效 target
```

---

## 11. Target Center 实验

目标从画面左侧移动到右侧时：

```text
target_x:
271
→ 330
→ 697
→ 1137
→ 1565
```

方向符合实际运动。

---

## 12. Bounding Box Center vs Moments Centroid

完整近似圆形目标：

```text
Target Center ≈ (670, 286)
Box Center ≈ (672, 287)
Delta ≈ (-2, -1)
```

遮挡后：

```text
Delta ≈ 7 ~ 8 px
```

说明轮廓质心会随着实际可见形状变化。

---

## 13. 遮挡实验

完整目标：

```text
Area ≈ 82,000 px²
```

遮挡后：

```text
Area ≈ 24,000 ~ 34,000 px²
```

同时：

- 轮廓碎片增加
- 质心发生变化
- Bounding Box 中心与 moments centroid 差异增大

结论：

```text
遮挡会改变面积和视觉质心
```

---

## 14. 无目标实验

已经完成。

完全移除橙色目标时：

```text
Contours = 0
Target Detected = False
```

还验证了：

```text
存在小橙色轮廓
Area ≈ 2800
MIN_TARGET_AREA = 5000
→ Target Detected = False
```

因此 roadmap 中“无目标场景测试”已完成。

---

## 15. 当前算法已知限制

当前实现只能称为：

```text
第一版受控环境基础检测器
```

不能称为最终鲁棒识别算法。

### 固定 HSV

更大的光照变化可能使颜色超出当前范围：

```text
H: 8 ~ 20
S: 150 ~ 255
V: 120 ~ 255
```

### 最大轮廓策略

当前代码：

```python
candidate = max(contours, key=cv2.contourArea)
```

意味着：

```text
最大的橙色区域
=
程序认为的目标
```

若出现比真实目标更大的橙色背景 / 物体，很可能误检。

### 固定面积门槛

```text
MIN_TARGET_AREA = 5000
```

可能导致远距离目标因面积变小而被拒绝。

### 遮挡

会导致：

- 面积下降
- 轮廓破碎
- 视觉质心变化

### 当前颜色不是“身份”

当前算法只能回答：

```text
哪个区域最符合当前颜色 + 面积规则？
```

还不能真正回答：

```text
哪个区域才是“我们定义的那个目标”？
```

---

## 16. Day 2 当前 Roadmap 状态

已完成：

```text
[x] BGR → HSV
[x] HSV 阈值分割
[x] 二值图
[x] 形态学处理
[x] 轮廓检测
[x] 选择有效目标
[x] 计算目标中心 (u, v)
[x] 在画面上显示目标位置
[x] 无目标场景测试
```

仍未完成：

```text
[ ] 更大同色干扰物场景测试
[ ] 更大光照变化和距离变化测试
[ ] Day 2 最终验收与阶段收尾
```

---

## 17. 下一步：更大同色干扰物实验

暂时不要修改代码。

实验目的：

证明当前规则：

```text
最大橙色轮廓 = 真正目标
```

并不可靠。

实验方法：

1. 保留当前真实橙色目标。
2. 在画面中加入面积明显更大的橙色物体。
3. 不修改代码。
4. 观察：
   - 绿色框是否跳到更大的橙色区域
   - 原目标是否被放弃
   - `Areas: [...]` 中最大的两个面积

预期可能得到：

```text
真正目标        ≈ 80,000 px²
大橙色干扰物    ≈ 150,000 px²

程序
→ 选择大橙色干扰物
```

如果出现这种结果，实验反而成功，因为它证明：

```text
颜色 + 最大面积
≠
目标身份
```

之后才根据失败现象学习新的特征，例如形状、长宽比、圆度、几何结构和多特征组合。

不要提前加入这些方法。

---

## 18. 暂时不要进入的内容

Day 2 完成前不要提前进入：

```text
Tracking
World Coordinate
Calibration / Homography
Motion Estimation
Kalman Filter
YOLO
Deep Learning
SLAM
ROS
复杂 GUI
```

原则：

```text
先亲眼看到问题
→ 理解为什么
→ 再增加最小必要方法
```

---

## 19. 学习协作方式

采用：

```text
边做项目边学习
```

规则：

1. ChatGPT 一次只给一个新的小步骤。
2. 先解释为什么做、新概念是什么、解决什么问题。
3. 用户亲自执行。
4. 用户提供截图、输出或实验现象。
5. ChatGPT 明确验收“通过 / 不通过”。
6. 验收后才进入下一步。
7. 不提前灌输后续高级知识。
8. 遇到新概念按需学习。

---

## 20. ChatGPT 与 Codex 分工

### ChatGPT 主要负责

- 新概念教学
- 算法理解
- 实验设计
- 失败现象分析
- 关键工程决策
- 一次一个新的学习步骤

### Codex 主要负责

已掌握的重复性工程工作，例如：

- `git status`
- `git diff`
- `git diff --check`
- `git add`
- staged diff 检查
- 常规 commit
- 常规 push
- README / AGENTS / roadmap / experiment_log 同步
- 常规代码与文档机械检查

### 仍需人工确认的危险 Git 操作

```text
git reset --hard
git clean
git rebase
git push --force
删除未合并分支
历史重写
```

---

## 21. 项目工程原则

```text
先验证
→ 再记录
→ 再 checkpoint
→ 再进入下一阶段
```

以及：

```text
先实验
→ 再重构
```

不要为了“看起来高级”而提前拆模块或引入复杂算法。

---

## 22. 新 ChatGPT 对话启动方法

新开对话时：

1. 上传本文件。
2. 最好同时上传：
   - `README.md`
   - `AGENTS.md`
   - `roadmap.md`
   - `docs/experiment_log.md`
3. 然后发送下面这段：

```text
这是 VisionMotion 项目的交接文件。

请先阅读 VisionMotion_HANDOFF.md，以及我上传的 README.md、AGENTS.md、
roadmap.md 和 docs/experiment_log.md。

继续使用项目原来的学习方式：
- 一次只教一个新的小步骤
- 先解释为什么和关键概念
- 我执行并发截图/输出
- 验收通过后再继续
- 已掌握的 Git 和常规文档流程交给 Codex
- 不提前进入 roadmap 后面的高级阶段

请从 HANDOFF 中记录的“下一步”继续，不要从头重新教学。
```

---

## 23. 以后让 Codex 更新 HANDOFF

每完成一个重要 checkpoint，可让 Codex：

```text
根据当前 README.md、AGENTS.md、roadmap.md、docs/experiment_log.md、
Git branch / log / status 和最新实验结果，更新 VisionMotion_HANDOFF.md。

要求：
- 只记录已经实际完成或验证的事实
- 不夸大算法能力
- 更新当前 branch / commit / stage
- 更新已完成与未完成 roadmap
- 更新下一步
- 保留 ChatGPT / Codex 协作规则
- 不修改 Python 代码
- 不自行 commit / push，除非明确要求
```

---

## 24. 当前一句话状态

```text
VisionMotion 已完成稳定手机摄像头输入和第一版 HSV 橙色目标检测，
当前正在 Day 2 验证“颜色 + 最大轮廓”策略的失效边界，
下一步是不改代码，加入更大的同色干扰物，亲自观察算法误检。
```
