"""
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,
他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。
现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何，
如果牌能组成顺子就输出true，否则就输出false。
为了方便起见,你可以认为大小王是0。

思路：
其实就是分两种情况，一种是四个王和1个数字，这样肯定是顺子；
另外一种就是多个数字，这时需要先对数字进行排序，对排序后的数字，
计算最大值和最小值之间的差值小于5
"""


def iscode(list_num):
    joker = 0
    list_num.sort()

    for i in range(len(list_num) - 1):
        if list_num[i] == 0:
            joker += 1
        elif list_num[i] == list_num[i + 1]:
            return 'false'
    return list_num[-1] - list_num[joker] < 5
