# show_cursor.py —— 给「看不见的指针」配一个看得见的替身标记
#
# 背景：webtop(Selkies) 把真实系统光标画在浏览器客户端、只跟随你的物理鼠标；
#       pyautogui 在底层移动的指针，它不画出来——所以脚本驱动鼠标时你看不到箭头滑。
#       这个脚本另开一个醒目小圆点，读真实指针位置、跟着它滑，画进桌面画面里，
#       于是脚本一动鼠标，画面里就看得到「光标在移动」（实时看和录屏都可见）。
#
# 用法：跑自动化脚本前，先在 webtop 桌面的终端里后台开着它——
#         python3 show_cursor.py &
#       再去跑 hello_world.py / w2_demo.py，就能看到小圆点跟着指针滑。
#       关掉它：pkill -f show_cursor.py
#
# 它只读指针位置、画自己，不碰鼠标键盘控制，安全。和 pyautogui 一样要在
# webtop 桌面的终端里跑（需要 DISPLAY=:1），别在 docker exec 的 shell 里跑。
import tkinter as tk

import pyautogui

DOT = 18          # 标记直径（像素）
OFFSET = 14       # 相对真实指针的偏移：摆到指针右下方，别盖住点击点
REFRESH_MS = 30   # 多久刷新一次位置（越小越跟手、越吃 CPU）

root = tk.Tk()
root.overrideredirect(True)             # 无边框、不被窗口管理器接管、不抢焦点
root.attributes("-topmost", True)       # 永远置顶
try:
    root.attributes("-alpha", 0.75)     # 半透明，需要桌面合成器；没有就当不透明，不影响功能
except tk.TclError:
    pass

canvas = tk.Canvas(root, width=DOT, height=DOT, highlightthickness=0, bg="white")
canvas.pack()
canvas.create_oval(2, 2, DOT - 2, DOT - 2, fill="#ff3b30", outline="white", width=2)


def follow():
    x, y = pyautogui.position()         # 真实指针位置（pyautogui 移动的就是它）
    root.geometry(f"{DOT}x{DOT}+{x + OFFSET}+{y + OFFSET}")  # 偏移摆放，不挡 (x, y) 的点击
    root.after(REFRESH_MS, follow)


follow()
root.mainloop()
