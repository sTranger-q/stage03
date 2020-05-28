"""
有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
    假如兔子都不死，问每个月的兔子总数为多少？
"""


# 幼崽: 1 0 1 1 2 3
# 成年: 0 1 1 2 3 5
# 总数: 1 1 2 3 5 8

def rabbit(month):
    if month == 1 or month == 2:
        number = 1
        return number
    else:
        return rabbit(month - 1) + rabbit(month - 2)


print(rabbit(5))
