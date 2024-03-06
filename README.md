# TRautoFish
开源的跑online自动化钓鱼脚本

[![][black-shield]][black]&nbsp;&nbsp;&nbsp;
[![][black-shield2]][black2]

[black]: https://discord.gg/JVH4QNYMXK
[black-shield]: https://img.shields.io/badge/DISCORD-JOIN-black.svg?style=for-the-badge&labelColor=gray

[black2]: https://im.qq.com
[black-shield2]: https://img.shields.io/badge/QQ_GROUP-718945618-black.svg?style=for-the-badge&labelColor=gray

# 功能
- 基于 [pyautogui](https://pypi.org/project/PyAutoGUI/0.9.53/) 的识图自动化脚本
- 游戏窗口自动前置
- 满背包自动收网
- 多进程处理钓鱼小游戏 **（医生蚯蚓/暮光蚯蚓）**
- 自动化重启游戏（可自定义）
- 根据配置文本自定义游戏键位
- 暂停运行热键: ``ctrl`` + ``f12``

# 如何使用发行版
1. 下载发行版[``TRautoFish.exe``](https://github.com/hiroshi-ya/TRautoFish/releases)（请根据实际情况选择版本）
2. 下载或自行创建配置文件[``autoPWD.txt``](https://github.com/hiroshi-ya/TRautoFish/releases)
3. 确保``TRautoFish.exe``和``autoPWD.txt``处于同一文件夹下
4. **参考[配置指南](#配置指南)编辑**``autoPWD.txt``
5. **参考[注意事项](#注意事项)**
6. 以管理员身份（系統管理員身分）运行``TRautoFish.exe``
7. 解放双手

# 配置指南
``autoPWD.txt``格式如下：
```
account   = 
password  = 
forward   = 
backward  = 
leftward  = 
rightward = 
jump      = 
item      = 
item2     = 
item3     = 
sprint    = 
```
- ``account = ``  后方输入你的游戏账号（可选，默认为不启用重启功能）
- ``password = `` 后方输入你的账号密码（可选，默认为不启用重启功能）
- ``forward = `` 后方输入你的前进按键（默认为``up``）
- ``backward = `` 后方输入你的后退按键（默认为``down``）
- ``leftward = `` 后方输入你的后退按键（默认为``left``）
- ``rightward = `` 后方输入你的后退按键（默认为``right``）
- ``jump = `` 后方输入你的跳跃按键（默认为``ctrl``）
- ``item = `` 后方输入你的道具按键（默认为``shift``）
- ``item2 = `` 后方输入你的道具2按键（默认为``a``）
- ``item3 = `` 后方输入你的道具3按键（默认为``s``）
- ``sprint = `` 后方输入你的冲刺按键（默认为``z``）
- **本脚本无法配置``runtime``**

### 注意：
- 文本文档中的空格都将被忽略，所以不需要对齐每一行
- 请确保不要修改（``account``等）关键词，修改关键词将导致配置失败
- 请确保不要去掉等号``=``
- 无效输入（如``4000+``、``@``、``XiGuSiMa``等）会被忽略并保持为默认设置
- 键位设置可以留空，留空即为默认设置
- 账号密码可以留空，留空即不开启脚本自动重启功能
- 按键配置中字母无视大小写（大写字母会被自动缩成小写）
- 多余的配置（如``eventMap``）不会被识别

# 注意事项
- 优先选择高性能版本
  1. 脚本分析游戏模式耗时应该在0.2秒左右，如果时长总是大于0.25秒说明电脑性能可能过低
  2. 电脑性能过低可能导致钓鱼游戏的准确率降低
  3. 如果高性能版本准确率过低则请尝试使用低性能版本
- **不支持 1024×768 游戏分辨率** ，其余分辨率（全屏/窗口化）皆可
- **游戏画面缩放会导致脚本识图不成功。** 请确保游戏画面没有被系统缩放
- **必须更改脚本的DPI设置：**
  1. 右键``TRautoFish.exe``
  2. 属性（內容）
  3. 兼容性（相容性）
  4. 更改高DPI设置（變更高DPI設定）
  5. 勾选替代高DPI缩放行为（覆寫高DPI縮放比例行為）-> 选择“应用程序”（“應用程式”）
  6. 确定 -> 确定
- 本程序会自动将游戏窗口前置，如需暂停脚本请按``ctrl`` + ``f12`` 激活暂停
- 如不想每次都点右键选管理员，可以：
  1. 右键``TRautoFish.exe``
  2. 属性（內容）
  3. 兼容性（相容性）
  4. 勾选``以管理员身份运行此程序``（``以系统管理員的身分執行此程式``）
  5. 确定，以后双击启动``TRautoFish.exe``即可
- **启用重启功能必须将游戏目录添加至环境变量（環境變數）：**
  1. Windows设置（設定）
  2. 系统
  3. 系统信息（系統資訊）
  4. 高级系统设置（進階系統設定）
  5. 高级（進階） -> 环境变量（環境變數）
  6. 在用户（使用者）变量或系统变量里寻找到``Path``变量（没有就自己新建一个``Path``）
  7. 编辑
  8. 新建，输入游戏启动器``talesrunner.exe``所在的目录（比如游戏处在``D:\TalesRunner\talesrunner.exe``的话就输入``D:\TalesRunner``）
  9. 确定 -> 确定 -> 确定
  10. 保存后，按下``win`` + ``r``，或者右键开始键 -> ``运行``（``執行``）
  11. 输入``talesrunner``并回车，可正常启动游戏启动器即设置成功
- **启用重启功能需禁用软件启动时的那个提示：**
  1. 开始菜单搜索``uac``
  2. 更改用户账户控制设置（變更使用者賬戶控制設定）
  3. 从不通知（不要通知）
  4. 确定
- **想要正确使用重启功能则必须使用“綠寶石海灘島”地形**
- **钓鱼状态栏必须处于高对比色区域（如图）**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![pre90](READMEpic/fishArea.png)

# 常见问题
***
> ### Win7能用吗？

大概率不行，因为高版本python不支持Win7了。你可以自行下载程序看是否可以打开。如果报错或无法运行，需要你自行解决。
***
> ### 32位系统能运行吗？

没测试过，可能不行。4202年了还在用32位系统？
***
> ### 你这脚本怎么这么占空间啊？

Python打包就是这样的，已经用upx压缩过了，嫌大你可以自己搭环境然后用Python运行源码
***
> ### 有毒吗？

开源的，你说呢？
***
> ### 用这玩意会被封号吗？

没有被EAC检测的可能。本程序不读取也不修改游戏客户端数据，亦不拦截/修改/伪造/发送网络封包，仅靠屏幕像素数据对关键图案进行识别。键鼠操作通过``DirectInput``键码以及调用Windows自带的``win32 API``实现，人畜无害。 ${\textbf{\color{red}但不排除}}$ 戏谷钓鱼执法，人肉探房的可能。 ${\textbf{\color{red}也不排除}}$ 戏谷人工查看后台游戏数据，根据游戏数据的异常状况（比如连着7×24小时不间用钓暮光蚯蚓）进行封禁。本程序对人肉探房/钓鱼执法无保护性措施，仅能自定义连续运行时长。本程序作者不对账号安全负责，不保证一定不会被封号。 ${\textbf{\color{red}风险自负}}$ 。

事实上，戏谷封禁脚本就只是一言堂而已，它们是没有扫盘的水准的，不如说整个戏谷的技术部门都不如栓一条狗来得靠谱。所谓的“不公平”其实就是口袋罪，它自己办了个钓鱼活动玩不起了就封你，平时你爱怎么钓鱼爱怎么挂机它不想管也没能力管。活动的时候收敛点就行，不然有连免费脚本都不愿意用的~贵物~眼红了上去举报你。

***
> ### 为什么必须要以管理员身份启动你的程序？

因为必须获取管理员权限才能让脚本实行游戏内键鼠操作。
***
> ### 运行时可以关掉屏幕的电源吗？

应该是可以的，但是请确保电脑不会息屏。另外，笔记本电脑在合上盖子后会强制息屏，所以在没有外接显示器的情况下大概是不能合上盖子的。
***
> ### 我担心在你的发行版脚本里输入账号密码不安全。

你可以选择不输入账密，不启用自动重启功能。
***
> ### 我想问的问题你这里没有解答。怎样向你反馈问题？

提issue，或者在discord频道/QQ群交流。欢迎任何PR，也欢迎你自个儿 fork 之后发行（请遵守GNU GPL v3.0）。请注意：**本人后续维护此脚本的可能性几乎为零**。

# Python解释环境

如果你想要自己用Python运行``autoRace.py``，以下是我环境的部分包：
```
python = 3.10.13
ahk = 1.5.0 # Require special treatment
opencv-python = 4.8.1.78
pyautogui = 0.9.53 # don't use later versions
numpy = 1.26.0
pillow = 9.5.0 # don't use later versions
pyinstaller = 6.0.0 # for packing exe
```
确保``scr``文件夹、``AutoHotkeyU64.exe``程序和``autoFish.py``处于一个目录下。
请注意，Python的``ahk``包至今有一个bug都没有修复，请参考[#263](https://github.com/spyoungtech/ahk/pull/263)自行修改``ahk``源文件。

在``gameModeDetect()``函数内调整性能版本：
- 使用``arrowB``即为高性能
- 使用``arrowG``即为低性能

打包使用 [pyinstaller](https://pypi.org/project/pyinstaller/) 、[upx](https://upx.github.io/) 以及 [Enigma Virtual Box](https://enigmaprotector.com/en/aboutvb.html) 。
