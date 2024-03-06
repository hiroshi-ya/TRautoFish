
import time
import pyautogui as gui
# import wmi
# import pydirectinput as key
# import pygetwindow as gw
# import keyboard
from ahk import AHK
from hashlib import blake2b
from multiprocessing import Process, freeze_support

def welcomeSequence():
    # eTime = expirationDate()
    print("\n***************************************************")
    print("* 欢迎使用跑Online全能钓鱼王!")
    print("* 请注意, 这是一个*免费*软件")
    print("* 如果你付费了, 不仅你被坑了, 作者也没收到任何收益")
    print("* 请确保您已阅读过使用说明")
    print("* 作者：文 (版本: autoFish低性能版)")
    print("***************************************************\n")
    return

def pauseFlagFlip():
# The function that flips the pauseFlag
    global pauseFlag
    pauseFlag = not pauseFlag
    if pauseFlag:
        ahk.sound_play('scr/pauseOn.mp3')
    else:
        ahk.sound_play('scr/pauseOff.mp3')
    return

def accessDeny():
# Basically an infinite loop to prevent access
    while True:
        time.sleep(1E6)

def restartSequence(enableRestart, infoList):
# This function is a sequence to restart the game

    trWin = ahk.find_window(title="Tales Runner")
    if trWin != None:
        print("\n* 尝试重启游戏")
        while trWin.exist:
            trWin.kill()
    else:
        print("\n* 尝试启动游戏")
        time.sleep(1)

    name = infoList[0]
    pwd  = infoList[1]

    while enableRestart and (ahk.find_window(title="Tales Runner") == None):
        ahk.set_clipboard("talesrunner")
        # win+r
        print("* 启动“运行”")
        ahk.send('#r')
        time.sleep(1)

        # Type "talesrunner"
        print("* 输入talesrunner并回车")
        ahk.send("^v")
        time.sleep(0.05)
        ahk.send('{enter}')
        print("* 等待20秒")
        time.sleep(20)

        # Press "enter" to start game
        print("* 敲击20次回车")
        for _ in range(20):
            ahk.send('{enter}')
            time.sleep(0.5)

        specialCase = False
        print("* 等待50秒")
        time.sleep(50)
        specialWin = ahk.find_window(title="TalesRunner")
        if specialWin != None:
            specialCase = True

        if specialCase: # error caused by zoom-in
            print("* 分辨率缩放导致的特有错误, 重新执行上方步骤")
            specialWin.activate()
            time.sleep(1)
            ahk.send('{enter}')
            time.sleep(1)
            # win+r
            ahk.send('#r')
            time.sleep(1)

            # Type "talesrunner"
            print("* 输入talesrunner并回车")
            ahk.send("talesrunner")
            time.sleep(0.05)
            ahk.send('{enter}')
            print("* 等待20秒")
            time.sleep(20)

            # Press "enter" to start game
            print("* 敲击20次回车")
            for _ in range(20):
                ahk.send('{enter}')
                time.sleep(0.5)

            print("* 等待50秒")
            time.sleep(50)
        
        trWin = ahk.find_window(title="Tales Runner")
        ahk.set_clipboard(name)
        if trWin != None: # game is launched
            trWin.activate()

            # Enter account info
            print("* 输入账号信息并回车")
            ahk.send("^v")
            ahk.send('{tab}')
            
            time.sleep(0.7)
            ahk.send(pwd, key_delay=70)
            time.sleep(0.7)

            ahk.send('{enter}')
            time.sleep(1)

            # Hit esc for 20 times
            print("* 敲击30次esc (一秒一次)")
            for _ in range(30):
                ahk.send('{esc}')
                time.sleep(1)

            if specialCase:
                ahk.send("!{enter}{enter}")
                time.sleep(2)
                ahk.send("!{enter}{enter}")
            
            ahk.mouse_move(10, 10)

        else:
            print("** 游戏启动失败, 尝试重新启动")
            for _ in range(3):
                ahk.send("{enter}")
                ahk.send("{esc}")
                time.sleep(0.1)

    if not enableRestart:
        print("** 未启用重启功能, 关闭游戏并停止工作 **")
        accessDeny()

    else:
        print("\n* 重启Tales Runner步骤执行完毕 *\n")
        trWin = ahk.find_window(title="Tales Runner")
        if trWin != None:
            trWin.activate()
        ahk.mouse_move(100, 100)
        toFishSequence(infoList[2])
        time.sleep(3)
    return

def toFishSequence(keyConfig):
# Try to go back to fishing position
    up      = keyConfig[0]
    down    = keyConfig[1]
    left    = keyConfig[2]
    right   = keyConfig[3]
    # z       = keyConfig[4]
    # x       = keyConfig[5]
    # c       = keyConfig[6]
    # a       = keyConfig[7]
    # d       = keyConfig[8]

    print("\n* 尝试重回农场")
    trWin = ahk.find_window(title='Tales Runner')
    topButtonPos = gui.locateCenterOnScreen("scr/topButton.png", confidence=0.89) # go to farm tab
    
    if topButtonPos != None:
        ahk.click(topButtonPos[0]+88, topButtonPos[1])
        time.sleep(1)
        ahk.send("{enter}")
        time.sleep(3)
        farmPos = gui.locateCenterOnScreen("scr/fish/myFarm.png", confidence=0.89)
        if farmPos != None: # go to my farm
            ahk.click(farmPos[0], farmPos[1])
            time.sleep(15)
            
            while True:
                if trWin == None:
                    print("** 你在搞毛啊, 游戏呢? **")
                    break
                windowRegion = trWin.get_position()

                print("* 蠕行至阴暗的角落")
                for _ in range(75):
                    ahk.key_down(up)
                    time.sleep(0.07)
                    ahk.key_up(up)
                    time.sleep(0.07)

                for _ in range(5):
                    ahk.key_down(left)
                    time.sleep(0.07)
                    ahk.key_up(left)
                    time.sleep(0.07)

                print("* 走向钓鱼点")
                ahk.key_down(down)
                ahk.key_down(right)
                time.sleep(1.38)
                ahk.key_up(down)
                ahk.key_up(right)

                time.sleep(10)
                print("* 等待10秒")
                readyPos = gui.locateCenterOnScreen('scr/fish/fishReady.png', confidence=0.89)
                readyNPos = gui.locateCenterOnScreen('scr/fish/fishReadyN.png', confidence=0.89)

                if readyNPos != None:
                    print("** 未到达钓鱼点, 打开农场商店重试")
                    shop = gui.locateCenterOnScreen('scr/fish/farmShop.png', confidence=0.89)
                    if shop != None:
                        ahk.click(shop[0], shop[1])
                        time.sleep(1)
                        crossPos = gui.locateOnScreen('scr/cross.png', confidence=0.89)
                        ahk.click(crossPos[0], crossPos[1])
                        time.sleep(5)
                elif readyPos != None:
                    print("* 成功走至钓鱼点")
                    ahk.click(readyPos[0], readyPos[1])
                    print("* 移动画面, 准备钓鱼")
                    ahk.mouse_move(windowRegion[0]+400, windowRegion[1]+400)
                    ahk.mouse_drag(800, 0, relative=True)
                    time.sleep(5)
                    break
                else:
                    print("** 不该这样的啊, 钓鱼按钮呢? 重启游戏吧")
                    trWin.kill()
                    break
        else:
            print("** 不该这样的啊, 我的农场按钮呢? 重启游戏吧")
            trWin.kill()
    else:
        print("** 不该这样的啊, 农场按钮呢? 重启游戏吧")
        trWin.kill()

def fishYZM(fishBag_fPos):
# Teleport fish by solving vf fish code
    print("\n* 正在将鱼传送至背包")

    # Click fishBag
    mousePos = gui.center(fishBag_fPos)
    ahk.click(mousePos[0], mousePos[1])
    time.sleep(3)

    # Click teleport fish
    telePos = gui.locateOnScreen('scr/fish/teleport.png', confidence=0.89)
    clickCount = 0

    while(telePos != None):
        mousePos = gui.center(telePos)
        ahk.click(mousePos[0], mousePos[1])

        time.sleep(1)
        clickCount = 0
        fishArr = [] # fishArr -> [(x-axis, fishName)]
        for s in "0123456789":
            fishShadow = gui.locateOnScreen('scr/fish/fish'+s+'_b.png', confidence=0.89)
            if fishShadow != None:
                fishArr.append((fishShadow[0], s))
                clickCount += 1
                if clickCount == 2:
                    break
        if clickCount == 2:
            if fishArr[0][0] > fishArr[1][0]: # Find the order, fishArr -> [fishName]
                fishArr = [fishArr[1][1], fishArr[0][1]]
            else:
                fishArr = [fishArr[0][1], fishArr[1][1]]
            for s in fishArr:
                fishPos = gui.locateOnScreen('scr/fish/fish'+s+'_f.png', confidence=0.89)
                if fishPos != None:
                    mousePos = gui.center(fishPos)
                    ahk.click(mousePos[0], mousePos[1])
                time.sleep(1)
        telePos = gui.locateOnScreen('scr/fish/teleport.png', confidence=0.89)
    return clickCount

def pressButton(buttonPos):
# Press the buttonPos button
    mousePos = gui.center(buttonPos)
    ahk.click(mousePos[0], mousePos[1])
    # time.sleep(1)
    return

def startFish(startFishPos):
# Try to start fishing
    if (startFishPos == None):
        print("** 异常情况(startFishPos == None) **")
        for _ in range(5):
            ahk.send('{esc}')
        # break
    else:
        print("* 开始钓鱼 *\n")
        mousePos = gui.center(startFishPos)
        ahk.click(mousePos[0], mousePos[1])
        time.sleep(1)
    return

def teleportFish(fishBag_fPos):
# Try to teleport fish
    global teleCount
    if fishYZM(fishBag_fPos) != 2: # Less than 2 fish recognized
        print("\n** 鱼验证码识别失败 **\n")
        for _ in range(3):
            ahk.send('{esc}')
    else:
        teleCount += 1
        print("* 已成功将鱼传送至背包\n* 传送次数:", teleCount)
    time.sleep(3)
    return

def changeBait(changeBaitPos):
    # Auto change bait
    print("* 鱼饵已用完\n* 尝试更换鱼饵")
    mousePos = gui.center(changeBaitPos)
    ahk.click(mousePos[0], mousePos[1])
    time.sleep(6)

    useBaitPos = gui.locateOnScreen('scr/fish/useBait.png', confidence=0.89)
    if useBaitPos == None: # No available bait in bag
        print("\n** 已无可用鱼饵 **\n")
        ahk.send('{esc}')
        accessDeny()
        # time.sleep(6)
        # buyBaitPos = gui.locateOnScreen('scr/fish/baitBuy.png', confidence=0.89)
        # buyBait(buyBaitPos)
    else:
        usingBatePos = None
        while usingBatePos == None:
            mousePos = gui.center(useBaitPos)
            ahk.click(mousePos[0], mousePos[1])
            usingBatePos = gui.locateOnScreen('scr/fish/usingBait.png', confidence=0.89)
            time.sleep(6)
        print("* 更换鱼饵成功")

    # final keyboard sequence
    ahk.send('{esc}')
    time.sleep(6)
    ahk.send('{esc}')
    time.sleep(6)
    return

def clearPrompt(windowRegion):
# Try to clear all the prompts in game
    changeBaitPos   = gui.locateOnScreen('scr/fish/baitBag.png', confidence=0.89, region=windowRegion)
    crossPos        = gui.locateOnScreen('scr/cross.png', confidence=0.89, region=windowRegion)
    okButtonPos     = gui.locateOnScreen('scr/okButton.png', confidence=0.89, region=windowRegion)
    denyPos         = gui.locateOnScreen('scr/denyInvite.png',confidence=0.89, region=windowRegion)
    
    if (okButtonPos != None):
    # Check if there is an OK button
        pressButton(buttonPos=okButtonPos)
        print("\n* 已发现并按下“确认”键 *\n")

    elif (denyPos != None):
    # Check if there is a deny button
        pressButton(buttonPos=denyPos)
        print("\n* 已发现并按下“取消”键 *\n")

    elif (crossPos != None):
    # Check if item expired
        pressButton(buttonPos=crossPos)
        print("\n* 已发现并按下“红叉” *\n")
    
    elif changeBaitPos != None:
        time.sleep(10)
        ahk.send("{enter}")
        time.sleep(0.5)
        changeBait(changeBaitPos)

    return

def gameAreaDetect():
    print("* 重新搜索读图区域中...")
    time0 = time.time()
    showTime = True
    while True:
        trWin = None
        while trWin is None:
            time.sleep(1)
            trWin = ahk.find_window(title="Tales Runner")
        windowRegion = trWin.get_position()
        startFishPos    = gui.locateOnScreen('scr/fish/startFish.png', confidence=0.89, region=windowRegion)
        startFishEndPos = gui.locateOnScreen('scr/fish/startFishEnd.png', confidence=0.89, region=windowRegion)

        if startFishEndPos is not None:
            locateArrowRegion = (startFishEndPos[0] - 244, startFishEndPos[1] - 61, 320, 48)
            locateDTypeRegion = (startFishEndPos[0] - 274, startFishEndPos[1] - 115+97, 350, 175-97)
            locateMovingRegion = (startFishEndPos[0] - 285, startFishEndPos[1] - 115, 361, 66)
            print("* 已获得搜索区域\n")
            break
        elif startFishPos is not None:
            locateArrowRegion = (startFishPos[0] - 241, startFishPos[1] - 59, 320, 48)
            locateDTypeRegion = (startFishPos[0] - 271, startFishPos[1] - 113+99, 350, 175-97)
            locateMovingRegion = (startFishPos[0] - 282, startFishPos[1] - 113, 361, 66)
            print("* 已获得搜索区域\n")
            break
        elif time.time() - time0 > 30 and showTime:
            print("\n** 超过30秒未识别到读图区域 **\n")
            showTime = False

    return (windowRegion, locateArrowRegion, locateDTypeRegion, locateMovingRegion)

def gameModeDetect():
# Detect if in game mode, constantly
    totalFish = 0
    dxPosList = [0]*3
    dIndexList = [0]*3
    windowRegion = None

    while True:
        trWin = ahk.find_window(title='Tales Runner')
        if trWin != None:
            checkRegion = trWin.get_position()
            if checkRegion != windowRegion:
                windowRegion, locateArrowRegion, locateDTypeRegion, locateMovingRegion = gameAreaDetect()

            dCount = 0
            check = time.time() # check tracking time

            for i in range(4): # tracking DType figs
                temp = gui.locateOnScreen('scr/fish/dType'+str(i)+'.png', region=locateDTypeRegion, confidence=0.8)
                if temp != None:
                    dxPosList[dCount] = temp[0]
                    dIndexList[dCount] = i
                    dCount = dCount + 1

            if dCount == 3: # found 3 DTypes, enter special mode
                print("* 分析游戏模式耗时: %.4f秒" % (time.time() - check))
                print("* 进入小游戏模式\n* 分析按键位置")

                i = 0  # for i in range(4)
                time0 = time.time() # time counter 1
                while True: # locate the moving DType's position (1/2/3)
                    temp = gui.locateOnScreen('scr/fish/dType'+str(dIndexList[i])+'.png', region=locateMovingRegion, confidence=0.3) # confidence = 0.3
                    if temp != None: # found
                        if dxPosList[i] == max(dxPosList): # right-most position
                            targetKey = '3'
                        elif dxPosList[i] == min(dxPosList): # left-most position
                            targetKey = '1'
                        else: # mid position
                            targetKey = '2'
                        print("* 目标位于: 第" + targetKey + "位")
                        print("* 分析目标耗时: %.4f秒" % (time.time() - time0))
                        ##################################################################
                        print("* 跟踪指针")
                        while True: # tracking the yellow-in-green arrow
                            time1 = time.time() # time counter 2
                            # arrowB = gui.locateOnScreen('scr/fish/arrowB2.png', region=locateArrowRegion, confidence=0.8)
                            arrowG = gui.locateOnScreen('scr/fish/arrowG.png', region=locateArrowRegion, confidence=0.65)
                            
                            # if arrowB == None:
                            if arrowG != None: # found the arrow
                                print("* 本次抓取总耗时: %.4f秒" % (time.time() - check))
                                ahk.send(targetKey)
                                totalFish = totalFish + 1
                                print("* 钓鱼游戏完成" + str(totalFish) + "次\n")
                                time.sleep(1)
                                break
                            elif time.time() - time1 > 30:
                                print("\n** 过长时间未跟踪到指针, 放弃跟踪 **\n")
                                break
                        break
                    elif time.time() - time0 > 30:
                        print("\n** 分析失败时间过长, 放弃本次分析 **\n")
                        break
                    else:
                        i = (0 if i==2 else i+1)
    return

def doctorLoop(infoList):
    if True: # just so I can collapse these initialization
        # Hotkey initialization
        global pauseFlag # Global pause flag, True = Pause program
        # pauseFlag = False
        ahk.add_hotkey('^F12', callback=pauseFlagFlip)
        ahk.add_hotkey('F12 & ctrl', callback=pauseFlagFlip)
        ahk.start_hotkeys()

        # Read user account info from the infoList
        usrName = infoList[0]
        usrPwd  = infoList[1]
        if usrName != '-1' and usrPwd != '-1':
            print("\n** 已启用自动重启功能\n** 请确保游戏目录已添加至环境变量的PATH中")
            print("** 账号: " + usrName)
            print("** 密码: " + usrPwd)
            print("** 若输入错误请关闭本程序并修改配置文件")
            enableRestart = True
            
        else:
            print("\n** 未识别到有效用户名&密码输入, 停用重启功能 **\n")
            enableRestart = False

    failTime = 0
    while True:
        if pauseFlag:
            print("\n** 暂停中, 再次按下 ctrl + f12 解除暂停 **")
            while pauseFlag:
                time.sleep(0.1)
            print("** 暂停已解除 **\n")
            continue

        trWin = ahk.find_window(title='Tales Runner')
        if trWin != None:
            trWin.activate() # front the window
            while not trWin.is_active(): # special cases
                ahk.send("!{Esc}")
                trWin.activate()
            windowRegion = trWin.get_position()
        else:
            restartSequence(enableRestart, infoList)
            continue

        # clearPrompt(windowRegion)
        fishBag_bPos    = gui.locateOnScreen('scr/fish/fishBag_b.png', confidence=0.89, region=windowRegion)
        fishBag_fPos    = gui.locateOnScreen('scr/fish/fishBag_f.png', confidence=0.89, region=windowRegion)
        startFishPos    = gui.locateOnScreen('scr/fish/startFish.png', confidence=0.89, region=windowRegion)

        if fishBag_bPos == None:
            if fishBag_fPos == None: # special case when fishBag icon disappears
                failTime += 1
                if failTime == 10: # cannot locate any icon, recapture window position
                    print("\n** 超过10秒未检测到关键图案 **")

                elif failTime >= 30:
                    print("** 超过30秒未检测到关键图案 **\n")
                    restartSequence(enableRestart, infoList)
                    failTime = 0
                else:
                    offline = gui.locateOnScreen('scr/offline.png', confidence=0.89, region=windowRegion)
                    if offline != None:
                        print("\n** 检测到已掉线 **")
                        restartSequence(enableRestart, infoList)
                        failTime = 0
            else:
                failTime = 0
                if startFishPos != None:
                    teleportFish(fishBag_fPos)
                
        else:
            failTime = 0
            if startFishPos != None:
                startFish(startFishPos)
        time.sleep(1)
        clearPrompt(windowRegion)
    return

def validKey(key:str):
    result = False
    length = len(key)
    if length == 1:
        if key.islower() or key.isnumeric():
            result = True
    elif length > 1:
        keyL = key.lower()
        if keyL in ['shift', 'ctrl', 'control', 'alt', 'tab', 'up', 'down', 'left', 'right']:
            result = True
    return result

def init():
# Program initialization:
# 1) check autoPWD
# 2) verify user's cdkey
# 3) return user's customized keyboard config and map selection
    try:
        print("* 尝试寻找并打开 autoPWD.txt")
        file = open("autoPWD.txt", 'r')
        print("* 成功打开 autoPWD.txt")
        
    except FileNotFoundError:
        try:
            file = open("autoPWD.txt.txt", 'r')
            print("* 成功打开 autoPWD.txt.txt")
            
        except FileNotFoundError:
            print("\n** 未找到 autoPWD.txt **\n")
            accessDeny()

    userInput = file.read().splitlines()
    
    # default values
    usrName     = '-1'
    usrPWD      = '-1'
    forward     = '{up}'
    backward    = '{down}'
    leftward    = '{left}'
    rightward   = '{right}'
    jump        = '{ctrl}'
    item        = '{shift}'
    item2       = '{a}'
    item3       = '{s}'
    sprint      = '{z}'
    runtime     = '21600'

    for s in userInput: # read various configuration
        # usrName (user's account)
        if s.find("account") != -1:
            try:
                temp = s.split('=')[1].replace(" ", "") # trim spaces
                if len(temp) != 0:
                    print("* 已读取用户名\t: " + temp)
                    usrName = temp
                else:
                    continue
            except IndexError:
                continue

        # usrPWD (user's password)
        elif s.find("password") != -1:
            try:
                temp = s.split('=')[1].replace(" ", "") # trim spaces
                if len(temp) != 0:
                    print("* 已读取密码\t: " + temp)
                    usrPWD = temp
                else:
                    continue
            except IndexError:
                continue

        # control - forward
        elif s.find("forward") != -1:
            try:
                temp = s.split('=')[1].replace(" ", "").lower() # trim spaces
                if validKey(temp):
                    print("* 已读取前进键\t: " + temp)
                    forward = "{" + temp + "}"
                else:
                    print("** 无效的前进键设置, 使用默认键位: " + forward)
            except IndexError:
                continue

        # control - backward
        elif s.find("backward") != -1:
            try:
                temp = s.split('=')[1].replace(" ", "").lower() # trim spaces
                if validKey(temp):
                    print("* 已读取后退键\t: " + temp)
                    backward = "{" + temp + "}"
                else:
                    print("** 无效的后退键设置, 使用默认键位: " + backward)
            except IndexError:
                continue

        # control - leftward
        elif s.find("leftward") != -1:
            try:
                temp = s.split('=')[1].replace(" ", "").lower() # trim spaces
                if validKey(temp):
                    print("* 已读取左拐键\t: " + temp)
                    leftward = "{" + temp + "}"
                else:
                    print("** 无效的左拐键设置, 使用默认键位: " + leftward)
            except IndexError:
                continue

        # control - rightward
        elif s.find("rightward") != -1:
            try:
                temp = s.split('=')[1].replace(" ", "").lower() # trim spaces
                if validKey(temp):
                    print("* 已读取右拐键\t: " + temp)
                    rightward = "{" + temp + "}"
                else:
                    print("** 无效的右拐键设置, 使用默认键位: " + rightward)
            except IndexError:
                continue

        # control - jump
        elif s.find("jump") != -1:
            try:
                temp = s.split('=')[1].replace(" ", "").lower() # trim spaces
                if validKey(temp):
                    print("* 已读取跳跃键\t: " + temp)
                    jump = "{" + temp + "}"
                else:
                    print("** 无效的跳跃键设置, 使用默认键位: " + jump)
            except IndexError:
                continue

        elif s.find("item2") != -1:
            try:
                temp = s.split('=')[1].replace(" ", "").lower() # trim spaces
                if validKey(temp):
                    print("* 已读取道具键2\t: " + temp)
                    item2 = "{" + temp + "}"
                else:
                    print("** 无效的道具键2设置, 使用默认键位: " + item2)
            except IndexError:
                continue

        elif s.find("item3") != -1:
            try:
                temp = s.split('=')[1].replace(" ", "").lower() # trim spaces
                if validKey(temp):
                    print("* 已读取道具键3\t: " + temp)
                    item3 = "{" + temp + "}"
                else:
                    print("** 无效的道具键3设置, 使用默认键位: " + item3)
            except IndexError:
                continue

        # control - item
        elif s.find("item") != -1:
            try:
                temp = s.split('=')[1].replace(" ", "").lower() # trim spaces
                if validKey(temp):
                    print("* 已读取道具键\t: " + temp)
                    item = "{" + temp + "}"
                else:
                    print("** 无效的道具键设置, 使用默认键位: " + item)
            except IndexError:
                continue

        # control - sprint
        elif s.find("sprint") != -1:
            try:
                temp = s.split('=')[1].replace(" ", "").lower() # trim spaces
                if validKey(temp):
                    print("* 已读取冲刺键\t: " + temp)
                    sprint = "{" + temp + "}"
                else:
                    print("** 无效的冲刺键设置, 使用默认键位: " + sprint)
            except IndexError:
                continue

    control = [forward, backward, leftward, rightward, jump, item, sprint, item2, item3]
    return [usrName, usrPWD, control, runtime]

def main():
    if __name__ == '__main__':
        freeze_support()
        welcomeSequence() # welcome
        infoList = init() # read txt file
        global teleCount # initialize fish teleport count
        teleCount = 0

        procClear = Process(target=gameModeDetect)  # instantiating clear prompt process
        procClear.start()

        doctorLoop(infoList)

ahk = AHK()
ahk.set_coord_mode('Mouse', 'Screen')
pauseFlag = False # Global pause flag, True = Pause program
main()

