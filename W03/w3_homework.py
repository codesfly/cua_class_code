# 作业1：补全 TODO 三处，让脚本读坐标清单、逐个安全点击、把成功/失败数写进日志
# 在 W1 沙箱桌面终端跑：python3 w3_homework.py
import time
import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3


def safe_click(x, y, retries=3, pause=1.0):
    for i in range(retries):
        try:
            # TODO 1: 点击坐标 (x, y)（用 pyautogui.click(x, y)），成功就 return True
            pass
        except Exception as e:
            print(f"第 {i+1} 次点击 ({x},{y}) 失败：{e}")
            time.sleep(pause)
    return False


def main():
    points = []
    with open("points.txt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y = line.split(",")
            points.append((int(x), int(y)))

    ok, fail = 0, 0
    # TODO 2: 用 for 遍历 points，对每个 (x, y) 调用 safe_click；
    #         成功 ok += 1，失败 fail += 1

    # TODO 3: 用 with open("w3_result.log", "a", encoding="utf-8") 把
    #         f"成功 {ok} 个，失败 {fail} 个\n" 追加写进日志
    print(f"完成：成功 {ok}，失败 {fail}")


if __name__ == "__main__":
    time.sleep(2)
    main()
