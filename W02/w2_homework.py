# 作业1：补全 TODO 两处，让鼠标在沙箱里按列表逐个点过去
import pyautogui, time
pyautogui.FAILSAFE = True

click_points = [(300, 200), (300, 400), (300, 600)]

def click_at(x, y, pause=0.5):
    # TODO: 移到 (x, y) 再点一下（用 pyautogui.moveTo + click）
    pass

time.sleep(2)
# TODO: 用 for 遍历 click_points，对每个坐标调用 click_at
