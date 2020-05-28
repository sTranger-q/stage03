"""
小明家必须要过一座桥。
小明过桥最快要１秒，小明的弟弟最快要３秒，
小明的爸爸最快要６秒，小明的妈妈最快要８秒，
小明的爷爷最快要１２秒。
每次此桥最多可过两人，而过桥的速度依过桥最慢者而定。
过桥时候是黑夜，所以必须有手电筒，小明家只有一个手电筒，而且手电筒的电池只剩30秒就将耗尽。
小明一家该如何过桥，请写出详细过程。

小明和弟弟:3S
小明回来:1S

妈妈和爷爷:12S

弟弟回来:3S

爸爸和小明:6S
小明回来:1S

小明和弟弟:3S
"""
import random

while True:
    # 左岸
    a = [1, 3, 6, 8, 12]
    # 右岸
    b = []
    STEP = 0
    # 存储单程时间
    step = []

    while True:
        x = random.sample(a, 2)
        print(x)
        b.extend(x)
        a.remove(x[0])
        a.remove(x[1])

        if x[0] > x[1]:
            step.append(x)
            step.append(x[0])

        else:
            step.append(x)
            step.append(x[1])

        if a == []:
            break
        y = random.sample(b, 1)
        a.extend(y)
        b.remove(y[0])
        step.append(y[0])

        step.append(">>>")
    for i in step:
        if type(i) == int:
            STEP += i
    if STEP <= 30:
        break

print(step)
print(STEP)
