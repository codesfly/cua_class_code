import time
import pyautogui

pyautogui.FAILSAFE = True   # 鼠标快速移到左上角可紧急中止
time.sleep(2)               # 留 2 秒切到桌面

# 让鼠标自己在桌面上画一个方块，证明"程序在操作这台机器"
points = [(200, 200), (600, 200), (600, 500), (200, 500), (200, 200)]
for x, y in points:
    pyautogui.moveTo(x, y, duration=0.5)

pyautogui.alert("Hello from your sandbox agent!")   # 弹窗收尾
