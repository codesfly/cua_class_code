# w2_demo.py —— 用「数据 + 循环 + 判断 + 函数」驱动鼠标
# 只在 webtop 浏览器画面里打开的那个终端跑：python3 w2_demo.py
#   别在自己电脑的终端跑，也别在 docker exec 进去的 shell 里跑——那两个连不上 webtop 桌面，鼠标不会动。
#   鼠标没反应？同一个终端先跑 check_display.py 自检（echo $DISPLAY 应是 :1，不是就 export DISPLAY=:1 再跑）。
#   看不到箭头自己滑是正常的：webtop 不画程序移动的系统光标。想看到移动，另开终端跑
#           python3 show_cursor.py &  会有个红点替身跟着指针滑；不开也能靠下面打印的坐标确认在动。
# 依赖 W1 已装的 pyautogui
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
    print("  指针现在在:", pyautogui.position())   # 坐标在变 = 鼠标真被程序挪了
    time.sleep(1)

print("跑完了，一共点了", len(click_points), "个点")
