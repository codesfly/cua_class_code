import time
import pyautogui

pyautogui.FAILSAFE = True   # 鼠标快速移到左上角可紧急中止
time.sleep(2)               # 留 2 秒切到桌面

# 让指针沿四个角走一圈，演示「程序在驱动这台机器的鼠标」。
# webtop 不会画出程序移动的系统光标，所以你看不到那个箭头自己滑——这正常。
# 想看到移动：另开一个终端先跑  python3 show_cursor.py &  会有个红点替身跟着指针滑。
# 不开替身也能确认在动：下面每步打印的坐标在变、结尾弹窗出现。
points = [(200, 200), (600, 200), (600, 500), (200, 500), (200, 200)]
for x, y in points:
    pyautogui.moveTo(x, y, duration=0.5)
    print("指针已移到:", pyautogui.position())   # 坐标每步在变 = 程序真的在动鼠标

pyautogui.alert("Hello from your sandbox agent!")   # 看到这个弹窗，就证明程序在操作这台机器
print("跑完了：看到弹窗 + 上面坐标在变，就是自动化成功了。")
