# W2 配套代码 · Python 速成①

对应教案《W2 · Python 速成①》。直接下载用，别手敲复制。

## 文件清单

| 文件 | 用途 | 怎么用 |
|---|---|---|
| `w2_demo.py` | 本周收尾脚本：列表 + for + if + 函数驱动鼠标 | 在 webtop 桌面终端跑 `python3 w2_demo.py`（依赖 W1 已装的 pyautogui） |
| `w2_homework.py` | 作业 1 起始框架（补全两处 TODO） | 补全 `click_at` 函数体和 for 循环，跑通让鼠标按列表逐个点 |
| `w2_cheatsheet.md` | 本周语法速查（变量 / 字符串 / 列表 / 字典 / for / if / 函数 各一例） | 随时翻查 |
| `check_display.py` | 跑脚本前的自检：确认这个终端连上了 webtop 桌面 | 鼠标不动时先跑 `python3 check_display.py`，看连没连上 |
| `show_cursor.py` | 给指针配个看得见的红点替身（想看鼠标滑动时用；同 W1 那份） | 跑 demo 前另开终端 `python3 show_cursor.py &`；关掉用 `pkill -f show_cursor.py` |

## 提醒

- 这些脚本要在 **webtop 浏览器画面里打开的那个终端**里跑（pyautogui 在 W1 已装好）。
- 跑 `w2_demo.py`，终端会按「数据 + 循环 + 判断 + 函数」逐步打印每一步（含每步鼠标坐标）——这是它第一次驱动真实操作。webtop 看不到那个系统箭头自己滑是正常的；想看到鼠标滑动，另开终端先跑 `python3 show_cursor.py &`（红点替身跟着指针滑），不开也能靠打印的坐标确认在动。
- **鼠标在 webtop 里没反应**：八成是脚本跑在了连不上 webtop 桌面的终端。pyautogui 要 `DISPLAY=:1` 才点得动 webtop——别在自己电脑的终端跑，也别在 `docker exec` 进去的 shell 里跑（那个 shell 默认没 `DISPLAY`）。先跑 `python3 check_display.py` 自检；临时救急在当前 shell `export DISPLAY=:1` 再跑。
