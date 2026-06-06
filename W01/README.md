# W1 配套代码 · 工具地基（沙箱 · SSH · Git）

对应教案《W1 · 开营 + 工具地基》。这里是可直接下载使用的文件——**别从正文里手敲复制**，容易漏字、复制错缩进。

## 文件清单

| 文件 | 用途 | 怎么用 |
|---|---|---|
| `sandbox/docker-compose.yml` | W1 隔离沙箱（Webtop，强制 X11） | 放进 `cua-camp/sandbox/`，在该文件夹 `docker compose up -d`，浏览器开 https://localhost:3001 |
| `hello_world.py` | 第一个自动化脚本（鼠标自己画方块） | 在沙箱桌面的终端里跑：先 `sudo apt update && sudo apt install -y python3-pip python3-tk scrot && pip3 install pyautogui` |
| `ssh-lab/docker-compose.yml` | 可选·方式 2：单独起 SSH 容器练手 ssh | 放进 `cua-camp/ssh-lab/`，在该文件夹 `docker compose up -d`，再 `ssh -p 2222 student@localhost` |
| `gitignore.txt` | `.gitignore` 模板 | 复制为 `cua-camp/.gitignore`（**去掉 `.txt` 后缀**） |

## 关键提醒

- **一个容器一个独立文件夹**：`cua-camp/sandbox/`（沙箱 compose + 数据卷 `sandbox-data/`）、`cua-camp/ssh-lab/`（可选）各自独立，compose 和它的数据都待在自己文件夹里，互不混、删起来干净。
- **`PIXELFLUX_WAYLAND=false` 这行别删**：pyautogui 注入鼠标键盘靠 X11，Selkies 默认走 Wayland 会打不动、截图黑、坐标点不准，W3/W4 的自动化全依赖它。
- **拉镜像慢就用 Clash 代理，别用国内镜像源**：镜像站只同步了一部分镜像，碰到它没收录或被过滤掉的就拉不到，还常年失效。开 Clash 的 Allow LAN，Docker Desktop → Settings → Resources → Proxies 填 `http://127.0.0.1:7890`（Windows 用 `http://host.docker.internal:7890`，端口以你 Clash 客户端为准），重启 Docker 后 `docker info` 能看到 `HTTP Proxy` 才算生效。
- **沙箱只是练习场**：本周里面怎么操作都不碰你的真系统；但 Agent 本身是会看错、点错的程序，等 W9 起真做能自己决策的 Agent，碰到删文件、改配置、花钱这类不可逆操作，必须留一道人类确认。
- **练 ssh 两种方式、二选一**：方式 1 给 webtop 直接装 sshd 连沙箱本体（改 `sandbox/docker-compose.yml` 的 `ports` 加 `2223:22`，再 `docker exec` 进容器装 sshd，无单独文件，步骤见教程 / 教案）；方式 2 用 `ssh-lab/docker-compose.yml` 起独立容器。日常拿沙箱 shell 仍用 `docker exec -it cua-sandbox bash`。
- **别把 3001 端口暴露到公网**（即使设了密码也不建议）。
