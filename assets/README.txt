一封可以走进去的信 · 素材规范（Asset Specification）
============================================================

本项目的核心规则：换视觉素材 ≠ 改交互逻辑。
你只需要：把素材放进对应目录 + 按本规范把规格告诉助手（或在代码 Assets 注册处登记），
程序自动替换，逻辑一行都不用动。

【1】目录结构
------------------------------------------------------------
assets/
  maps/            map_classroom.png        ← 完整地图整图（可选）
  characters/      player_cat.png           ← 小猫（Sprite Sheet 或单图）
  ui/              ui_dialogue.png / ui_popup.png / ui_button_*.png   （预留）
  memory-objects/  memory_peach.png / memory_textbook.png   ← 记忆物件（透明 PNG）
  memory-content/  memory_peach_01.jpg      ← 记忆里的真实照片 / 卡片
  effects/         effect_rain.gif / .webm / 多帧 / sprite   （预留，类型待定）
  audio/           bgm_*.mp3 / sfx_*.wav    ← 音乐 / 音效

【2】语义 ID 与素材对应
------------------------------------------------------------
逻辑层只认语义 ID，不认文件名。当前使用的 ID：
  map_classroom        地图整图        → assets/maps/map_classroom.png
  player_cat           小猫            → assets/characters/player_cat.png
  memory_peach         桃子物件        → assets/memory-objects/memory_peach.png
  memory_textbook      课本物件        → assets/memory-objects/memory_textbook.png
  memory_content_peach_01  桃子记忆的照片 → assets/memory-content/memory_peach_01.jpg

预留（接口已定义，需要时接入）：
  ui_dialogue / ui_popup / ui_button_* / effect_rain / bgm_* / sfx_*

【3】素材格式要求
------------------------------------------------------------
- 透明背景：角色 / 物件 / 效果用 PNG；真实照片用 JPG 或 PNG；UI 皮肤 PNG 或 SVG。
- 尺寸：地图和角色的 16px 网格只是当前技术参数，不是全项目规范。
  UI、照片、弹窗、动态效果按你的设计自由定尺寸。
  地图整图尺寸与碰撞网格保持同比例（当前 30×18 格 → 480×288 或 960×576 等整数倍），
  程序会按画布缩放铺满，碰撞仍按网格数据。
- 小猫 Sprite Sheet：默认按 4 行（下/上/右/左）× 2 列（走帧）切分；帧尺寸、行顺序、fps
  都可在 Assets 注册处改（告诉助手即可）。
- 动画帧率：像素风建议 6–12 fps；循环动画首尾帧无缝。
- 命名：语义 ID 为准，多帧加序号（rain_01.png），提供时附一句规格（尺寸/帧率/循环/锚点）。

【4】动态素材：先定类型，不写死
------------------------------------------------------------
一个动态效果（如下雨）未来可能是这几种之一，接口全部兼容：
  A. GIF        → 直接放进 effects/，当图播放
  B. Sprite Sheet → 放单张含帧图，按帧切
  C. 多帧序列   → rain_01.png / rain_02.png / rain_03.png，循环播放
  D. WebM       → 视频循环（适合复杂背景 / 粒子氛围层）
  E. 程序生成   → 不需要素材，写参数即可（适合规律、轻量的像素雨滴 / 闪光）
不确定用哪种时，先在对话里告诉我效果，我们定类型后再给素材。

【5】最小替换示例
------------------------------------------------------------
例子：把桃子换成你自己的图。
  1) 把图放到 assets/memory-objects/memory_peach.png（透明 PNG）
  2) 如果显示尺寸想改，告诉助手：Assets 里 memory_peach 的 size 改成 [宽, 高]
  3) 完成。掉落、点击、弹窗全部自动用你的图。
同理：小猫 / 地图整图 / 弹窗里的真实照片，都是"放文件 + 登记规格"。
