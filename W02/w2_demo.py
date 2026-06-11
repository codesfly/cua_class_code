# w2_demo.py —— 用「数据 + 循环 + 判断 + 函数」驱动鼠标
# 在 W1 沙箱桌面的终端里跑：python3 w2_demo.py（依赖 W1 已装的 pyautogui）
import pyautogui, time

pyautogui.FAILSAFE = True   # 鼠标快速移到左上角可紧急中止

def click_at(x, y, duration=0.5):
    """移到 (x, y) 再点一下"""
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()

# 一批要依次点击的坐标（列表）
click_points = [(200, 300), (450, 300), (700, 300)]

time.sleep(2)               # 留 2 秒切到沙箱桌面
for x, y in click_points:   # 逐个取出
    if x < 500:             # 看情况办事
        print("点左半边:", x, y)
    else:
        print("点右半边:", x, y)
    click_at(x, y)          # 复用封装好的动作
    time.sleep(1)

print("跑完了，一共点了", len(click_points), "个点")
