# CUA 训练营 · 配套代码

《从零到自建 Computer Use Agent · 16 周实战训练营》各周配套代码，按周分类。
直接下载对应周的文件夹使用，别从课程正文手敲复制。

## 目录

- `W01/` — 工具地基（沙箱 · SSH · Git）
  - `docker-compose.yml` — 一键起隔离沙箱（Webtop，强制 X11）
  - `daemon.json` — 国内镜像加速模板
  - `hello_world.py` — 第一个自动化脚本（鼠标自己画方块）
  - `ssh-lab.yml` — 可选：用 ssh 连本地容器练手
  - `gitignore.txt` — `.gitignore` 模板（复制时去掉 .txt 后缀）
- `W02/` — Python 速成①（变量 / 列表 / 字典 / for / if / 函数）
  - `w2_demo.py` — 列表 + for + if + 函数驱动鼠标的收尾脚本
  - `w2_homework.py` — 作业 1 起始框架（补全两处 TODO）
  - `w2_cheatsheet.md` — 本周语法速查
- `W03/` — Python 速成② + 第一个 pyautogui（文件读写 / import / try-except / pyautogui）
  - `w3_demo.py` — 读坐标清单 → 逐个安全点击（带重试）→ 写日志的收尾脚本
  - `points.txt` — `w3_demo.py` 读的坐标清单（一行一个 `x,y`）
  - `w3_homework.py` — 作业 1 起始框架（补全三处 TODO）
  - `w3_cheatsheet.md` — 本周语法速查

后续每周陆续补充。
