# 作业1：补全 TODO 两处，让鼠标在沙箱里按列表逐个点过去
# 跑起来怎么算成功：看终端按坐标逐个打印（webtop 看不到箭头自己滑，正常）。
# 想看到鼠标滑动：另开终端先跑  python3 show_cursor.py &  （W1 配套，红点替身跟着指针滑）。
import pyautogui, time
pyautogui.FAILSAFE = True

click_points = [(300, 200), (300, 400), (300, 600)]

def click_at(x, y, duration=0.5):
    # TODO: 移到 (x, y) 再点一下（用 pyautogui.moveTo(x, y, duration=duration)，再 pyautogui.click()）
    pass

time.sleep(2)
# TODO: 用 for 遍历 click_points，对每个坐标调用 click_at
