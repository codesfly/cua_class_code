# W3 语法速查 · Python 速成② + 第一个 pyautogui

文件读写、import、try/except、pyautogui 各留一例，随时翻查。

```python
import time
import pyautogui
import pyperclip

# 文件读写：读一行一个目标、写日志（一律带 encoding）
targets = []
with open("targets.txt", encoding="utf-8") as f:
    for line in f:               # 逐行读
        line = line.strip()      # 去首尾空格 / 换行
        if line:                 # 跳过空行
            targets.append(line)
with open("result.log", "a", encoding="utf-8") as f:         # a 追加、w 覆盖
    f.write("处理完成\n")

# import + pip：标准库自带，第三方库先 pip3 install 再 import
print(pyautogui.size())          # 确认 pyautogui 装好、能读屏幕

# try / except：接住报错，重试而不是崩
def safe_click(x, y, retries=3, pause=1.0):
    for i in range(retries):
        try:
            pyautogui.click(x, y)
            return True
        except Exception as e:
            print(f"第 {i+1} 次失败：{e}")
            time.sleep(pause)
    return False

# pyautogui：移动 / 点击 / 输入 / 按键 / 截图 / 找图
pyautogui.FAILSAFE = True        # 鼠标移到左上角 → 急停
pyautogui.PAUSE = 0.5            # 每步之间自动停
pyautogui.moveTo(300, 300, duration=0.5)
pyautogui.click()
pyautogui.write("hello", interval=0.05)   # 只支持英文 / ASCII
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "s")
pyautogui.screenshot("shot.png")
pos = pyautogui.locateCenterOnScreen("button.png", confidence=0.9)  # 找不到返回 None

# 中文输入：write 不支持中文，走剪贴板粘贴
pyperclip.copy("你好，世界")     # Linux 沙箱首次用需 sudo apt install xclip
pyautogui.hotkey("ctrl", "v")   # macOS 用 "command", "v"
```
