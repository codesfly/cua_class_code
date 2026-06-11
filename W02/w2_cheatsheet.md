# W2 语法速查 · Python 速成①

只列做 Agent 早期用得上的几样，随时翻查。

```python
import pyautogui

# 变量 / 字符串 / 数字
app_name = "记事本"      # 字符串带引号
wait = 2                 # 数字不带引号
greeting = "Hi, " + app_name   # 字符串用 + 拼接

# 列表：一排有顺序的东西，下标从 0 开始
pts = [(200, 300), (450, 300)]
print(pts[0])            # (200, 300)
print(len(pts))          # 2 —— 列表里有几个

# 元组：固定搭配的一组值，用 ()，坐标就是元组
point = (200, 300)
print(point[0], point[1])   # 200 300

# 字典：带标签的一组值，按 key 取
task = {"name": "导出", "retry": 3}
print(task["name"])      # 导出

# for + 解包：每个元素是 (x, y) 元组，一次拆给 x、y
for x, y in pts:
    print(x, y)

# if / else：看情况办事
if wait > 1:
    print("等久一点")
else:
    print("很快")

# 函数：封装一段动作，换参数复用
def click_at(x, y, duration=0.5):
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()
```
