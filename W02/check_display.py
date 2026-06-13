# check_display.py —— 跑自动化脚本前，先确认这个终端连上了 webtop 桌面
# 用法：在你准备跑 w2_demo.py 的同一个终端里，先跑一次：python3 check_display.py
# 它只读环境、不动鼠标，安全。打出「✓ 连上了」再去跑 w2_demo.py。
import os

display = os.environ.get("DISPLAY")
print("DISPLAY =", repr(display))

if not display:
    print()
    print("✗ 这个终端没有 DISPLAY，连不上 webtop 桌面，鼠标不会动。")
    print("  你大概率在自己电脑的终端、或 docker exec 进来的 shell 里——这两个都连不上 webtop。")
    print("  正确做法：在 webtop 浏览器画面里打开的那个终端跑脚本；")
    print("  临时救急：先执行  export DISPLAY=:1  再重跑本脚本。")
    raise SystemExit(1)

try:
    import pyautogui
except ImportError:
    print()
    print("✗ 没装 pyautogui（W1 沙箱里应已装好）：")
    print("  pip3 install pyautogui   # 报 externally-managed 就加 --break-system-packages")
    raise SystemExit(1)

try:
    width, height = pyautogui.size()
    x, y = pyautogui.position()
except Exception as e:
    print()
    print("✗ pyautogui 连不上 X11 显示：", e)
    print("  多半是 webtop 跑成了 Wayland。确认 compose 里有 PIXELFLUX_WAYLAND=false，再重建容器。")
    raise SystemExit(1)

print(f"屏幕尺寸 = {width} x {height}")
print(f"当前鼠标 = ({x}, {y})")
print()
print("✓ 连上了。这个终端能驱动 webtop 桌面，可以跑 w2_demo.py 了。")
