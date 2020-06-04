"""
1.1 对一组数完成快速排序

快速排序，又称划分交换排序，从无序队列中挑取一个元素，把无序队列分割成独立的两部分，
其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，
整个排序过程可以递归进行，以此达到整个数据变成有序序列。 简单来说：挑元素、划分组、分组重复前两步

思路

快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。

步骤为：

- 挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;
- 分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成;
- 递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。

递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。

选取基准值有数种具体方法，此选取方法对排序的时间性能有决定性影响。
"""

list01 = [1, 23, 54, 1, 7, 87, 123, 543, 763, 23, 12, 43, 1, 2, 56, 12]


# def partition(list_target, left, right):
#     pivot = list_target[right]
#     index = left - 1
#     for i in range(left, right):
#         if list_target[i] <= pivot:
#             index += 1
#             list_target[i], list_target[index] = list_target[index], list_target[i]
#     list_target[right], list_target[index + 1] = list_target[index + 1], list_target[right]
#     return index + 1
#
#
# def quick_sort(list_target, left, right):
#     if left < right:
#         pivot = partition(list_target, left, right)
#         partition(list_target, left, pivot - 1)
#         partition(list_target, pivot + 1, right)


def partition(list_target, left, right):
    index = right + 1
    pivot = list_target[left]
    for i in range(right, left, -1):
        if list_target[i] >= pivot:
            index -= 1
            list_target[i], list_target[index] = list_target[index], list_target[i]
    list_target[left], list_target[index - 1] = list_target[index - 1], list_target[left]
    return index - 1


def quick_sort(list_target, left, right):
    if left < right:
        pivot = partition(list_target, left, right)
        quick_sort(list_target, left, pivot - 1)
        quick_sort(list_target, pivot + 1, right)


quick_sort(list01, 0, len(list01) - 1)
print(list01)
