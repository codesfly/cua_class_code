# w3_demo.py —— 读清单、逐个安全点击、出错重试、写日志
# 在 W1 沙箱桌面的终端里跑：python3 w3_demo.py（依赖 pyautogui，W1 已装）
import time
import pyautogui

pyautogui.FAILSAFE = True       # 鼠标快速移到左上角可紧急中止
pyautogui.PAUSE = 0.3           # 每个动作后自动停一下


def safe_click(x, y, retries=3, pause=1.0):
    """点 (x, y)，失败重试 retries 次；都失败返回 False，不中断整个流程。"""
    for i in range(retries):
        try:
            pyautogui.click(x, y)
            return True
        except Exception as e:
            print(f"第 {i+1} 次点击 ({x},{y}) 失败：{e}")
            time.sleep(pause)
    return False


def main():
    # 从文件读坐标：每行 "x,y"
    points = []
    with open("points.txt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y = line.split(",")           # 按逗号拆成 "300"、"300"（还是字符串）
            points.append((int(x), int(y)))  # int() 把字符串转成数字

    ok, fail = 0, 0
    for x, y in points:
        if safe_click(x, y):
            ok += 1
        else:
            fail += 1

    with open("w3_result.log", "a", encoding="utf-8") as f:
        f.write(f"成功 {ok} 个，失败 {fail} 个\n")
    print(f"完成：成功 {ok}，失败 {fail}")


if __name__ == "__main__":      # 固定写法：直接运行本文件时才执行，照抄即可
    time.sleep(2)               # 留 2 秒切到沙箱桌面
    main()
