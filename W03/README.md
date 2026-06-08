# W3 配套代码 · Python 速成② + 第一个 pyautogui

对应教案《W3 · Python 速成② + 第一个 pyautogui demo》。直接下载用，别手敲复制。

## 文件清单

| 文件 | 用途 | 怎么用 |
|---|---|---|
| `w3_demo.py` | 本周收尾脚本：读坐标清单 → 逐个安全点击（带重试）→ 写日志 | 在 W1 沙箱桌面终端跑 `python3 w3_demo.py`（依赖 W1 已装的 pyautogui） |
| `points.txt` | `w3_demo.py` 读的坐标清单，一行一个 `x,y` | 和 `w3_demo.py` 放同一目录；改清单不用改代码 |
| `w3_homework.py` | 作业 1 起始框架（补全三处 TODO） | 补全 `safe_click`、for 循环、写日志三处，跑通 |
| `w3_cheatsheet.md` | 本周语法速查（文件读写 / import / try-except / pyautogui 各一例） | 随时翻查 |

## 提醒

- 这些脚本要在 **W1 的沙箱桌面**里跑（环境和后面一致；pyautogui 在 W1 已装好）。
- 在 Linux 沙箱里，两个一次性系统依赖按需补：中文剪贴板粘贴需要 `sudo apt install -y xclip`；截图 / 找图需要 `sudo apt install -y scrot`。
- 跑 `w3_demo.py` 会看到鼠标按 `points.txt` 里的坐标依次移动、点击——出错会自动重试，跑完把成功 / 失败数写进 `w3_result.log`。
