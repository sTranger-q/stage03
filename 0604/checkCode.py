"""
1.5 某产品的用户注册邀请码为一串有小写字母和数字组成的字符串，字符串长度为16，
当用户数据邀请码的时候，系统需要对邀请码做有效性验证，假设验证规则如下

1、从序列号最后一位字符开始，逆向将奇数位（1、3、5等等）相加；

2、从序列号最后一位数字开始，逆向将偶数位数字，先乘以2（如果乘积为两位数，则将其减去9），再求和；

3、将奇数位总和加上偶数位和，结果可以被10整除；

4、小写字母对应数值，可由下面键值对确定；

[(a,1),(b,2),(c,3).....(i,9),(j,1),(k,2).....],按照字母排序，1-9循环

输入：输入16位字符串，表示邀请码

输出：输出‘ok’或者‘error’
"""
dict01 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
          'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9,
          's': 1, 't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8,
          '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def code(code: str):
    # 奇数
    odd = 0
    # 偶数
    even = 0
    if len(len(code) != 16):
        return 'error'
    for i in range(len(code) - 1, -1, -2):
        if code[i] in dict01:
            odd += dict01[code[i]]
        else:
            return 'error'
    for i in range(len(code) - 2, -1, -2):
        if code[i] in dict01:
            result = dict01[code[i]] * 2
            if result >= 10:
                result -= 9
            even += result
        else:
            return 'error'
    if (odd + even) % 10 == 0:
        return 'OK'
    else:
        return 'error'

