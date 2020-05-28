list1 = [88,2,32,12,86,23,34,124]

# def bubbleSort(arr):
#     for i in range(1,len(arr)):
#         for j in range(0,len(arr)-i):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr
#
#
# a = bubbleSort(list1)
# print(a)

# def insert(list_):
#     for i in range(1,len(list_)):
#         x = list_[i]
#         j = i - 1
#         while j >= 0 and list_[j] > x:
#             list_[j+1] = list_[j]
#             j -= 1
#         list_[j+1] = x
#     return list_
#
# b = insert(list1)
# print(b)

# def select(list_):
#     for i in range(len(list_)-1):
#         # 定义最小值
#         min = i
#         for j in range(i+1,len(list_)):
#             if list_[min] > list_[j]:
#                 min = j
#         if min != i:
#             list_[i],list_[min] = list_[min],list_[i]
#     return list_
#
# c = select(list1)
# print(c)

# 幼崽 1 0 1 1 2 3
# 成年 0 1 1 2 3 5
# 总数 1 1 2 3 5 8
#f(n) = f(n-1) + f(n-2)
# def fc_seq(i):
 #     list1 =[1,1]
#     for item in range(i):
#         if item > 1:
#             list1.append(list1[item-1]+list1[item-2])
#     print('第{}个月的兔子的总数{},兔子的明细{}'
#           .format(i,sum(list1[0:i]),list1))
#     print("%s,%s"%('a','c'))
#
# d = fc_seq(3)

"""
小明家必须要过一座桥。小明过桥最快要１秒，
小明的弟弟最快要３秒，小明的爸爸最快要６秒，
小明的妈妈最快要８秒，小明的爷爷最快要１２秒。
每次此桥最多可过两人，而过桥的速度依过桥最慢者而定。
过桥时候是黑夜，所以必须有手电筒，小明家只有一个手电筒，
而且手电筒的电池只剩30秒就将耗尽。小明一家该如何过桥，请写出详细过程。

小明和弟弟　３s
小明　　　　１s

妈妈和爷爷　12s
弟弟　　　　３ｓ

爸爸和小明　６ｓ
小明　　　　１ｓ

小明和弟弟　３ｓ
"""
print(3+1+12+3+6+1+3)

import random
while True:
    # 左岸
    a = [1,3,6,8,12]
    # 右岸
    b = []
    STEP = 0
    # 存储单程时间
    step = []

    while True:
        x = random.sample(a,2)
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

        y = random.sample(b,1)
        a.extend(y)
        b.remove(y[0])
        step.append(y[0])

        step.append('>>')

    for i in step:
        if type(i) == int:
            STEP = STEP + i

    if STEP <= 30:
        break

print(step)
print(STEP)
