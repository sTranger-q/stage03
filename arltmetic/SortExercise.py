list01 = [1, 3, 4, 2, 1, 5, 6, 7, 8, 1, 10, 123, 2, 34]


# 1.对一组数完成冒泡排序
def bubbling():
    for r in range(len(list01) - 1):
        flag = True
        for c in range(1, len(list01) - r):
            if list01[c - 1] > list01[c]:
                list01[c - 1], list01[c] = list01[c], list01[c - 1]
                flag = False
        if flag:
            return


#
# bubbling()
# print(list01)


# 2.对一组数完成插入排序
def insert():
    for i in range(1, len(list01)):
        mark = list01[i]
        index = i - 1
        while index >= 0 and list01[index] > mark:
            list01[index + 1] = list01[index]
            index -= 1
        list01[index + 1] = mark


insert()
print(list01)


# 3.对一组数完成选择排序
def chose():
    for r in range(len(list01) - 1):
        for c in range(r + 1, len(list01)):
            if list01[r] > list01[c]:
                list01[r], list01[c] = list01[c], list01[r]
