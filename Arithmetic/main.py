# import time
# from datetime import datetime
# import datetime
# import re
import random
from fraction import Fraction
from random import choice

'''# 删除字符串中的标点符号
def Remove_punctuation(data):
    data1 = []
    remove_chars = '-.:'
    string = re.sub(remove_chars, "", data)
    data1.append(string)
    return data1


# 通过当前时间生成hash的函数
def Generate_hash():
    now = str(datetime.datetime.now())
    now = str(Remove_punctuation(now))  # 去除时间中的多余的符号
    now = now.replace("[", "").replace("'", "").replace(" ", "").replace("'", "'").replace("]", "")  # 将空格与[]符号去除
    hash1 = hash(now)
    if hash1 < 0: hash1 = -hash1
    return hash1'''

'''# 连接两个数字的函数
def Stitching_Numbers(num1, num2):
    global str1
    if (type(num1) == int): str1 = str(num1)
    if (type(num2) == int): str2 = str(num2)
    str3 = str1 + str2
    return str3


# 创建序列号函数

def Get_serial_number():
    num1 = Generate_hash()
    time.sleep(0.2)  # 等待0.2s,以便于生成两个不同的哈希值
    num2 = Generate_hash()
    serial = Stitching_Numbers(num1, num2)
    return serial'''

# 设置全局变量
NUM = 0


# 文件写入函数
def Create_txt(name, msg, model):
    if model == 1:  # 模式1:创建txt文件以及序列号
        name = name + ".txt"
        with open(name, "a+") as file1:
            file1.write(msg + "\n")
            file1.close()

    return 0


# 在序列号中添加题目数量函数
def Add_num(quantity, serial, num):
    str1 = "0"
    str2 = ""
    if len(quantity) < num:
        for i in range(0, num - len(quantity)):
            str2 += str1
    quantity = str2 + quantity
    serial = quantity + serial
    return serial


# 获取生成题目数量的函数
def Get_quantity():
    # 判断字符串是否大于5的函数
    def Judge_len(str1):
        if len(str1) > 5:
            return False
        else:
            return True

    state = False
    quantity = input("请输入题目的数量(10000以内):")
    state = quantity.isnumeric() and Judge_len(quantity)
    while state == False:
        print("输入有误!请重新输入:")
        quantity = input()
        state = quantity.isnumeric() and Judge_len(quantity)
    return quantity


# 获取生成题目的范围
def Get_range():
    def Judge_len(str1):
        if len(str1) > 3:
            return False
        else:
            return True

    numrange = input("请输入题目数字的大小范围(1000以内):")
    state = numrange.isnumeric() and Judge_len(numrange)

    while state == False:
        print("输入有误!请重新输入:")
        numrange = input()
        state = numrange.isnumeric() and Judge_len(numrange)
    return numrange


# 生成整数的函数
def Create_integer(serial):
    numrange = int(serial[4:7])
    intrger = random.randint(1, numrange)
    return intrger


# 生成分数的函数
def Create_fraction(serial):
    # 这里的比较是为了让生成的分数不能被化简为整数
    def Judge_num(num1, num2, max):
        if num1 < num2:
            return True
        else:
            for i in range(1, int(max / num2)):
                if i * num2 == num1: return False
            else:
                return True

    numrange = int(serial[4:7])
    intrger1 = random.randint(1, numrange)
    intrger2 = random.randint(1, numrange)
    frac = Fraction(intrger1, intrger2)
    while Judge_num(intrger1, intrger2, numrange) == False:
        intrger1 = random.randint(1, numrange)
        intrger2 = random.randint(1, numrange)
        frac = Fraction(intrger1, intrger2)
    return frac


'''
1、同两个数 加减乘除一起（数量无法均匀分配 遇到-和/要另外处理）
2、不同数 加减乘除随机（查重比较麻烦）
'''


# 从随机整数/分数序列中选一个数字参与运算
def num_choice(serial):
    list1 = [Create_fraction(serial), Create_integer(serial)]
    return choice(list1)


# 选择运算符
def op_choice():
    list2 = ['+', '-', '*', '/']
    return choice(list2)


# 分数化简为整数/带分数
def real_fra(a):
    if a > 1:
        x = a.numerator  # 获取分子
        y = a.denominator  # 获取分母
        num1 = x // y  # 整数部分
        num2 = x % y  # 余数
        if num2 == 0:  # 答案为整数
            a = num1
        else:
            num1 = str(num1)
            num2 = str(Fraction(num2, y))
            a = num1 + "'" + num2
        return a
    else:
        return a


# 四则运算
def function():
    global NUM
    NUM = NUM + 1
    x = num_choice(serial)
    y = num_choice(serial)
    op = op_choice()

    if op == '+':
        a = Fraction(x) + Fraction(y)
        a = real_fra(a)
        print(NUM, '. {} + {} ={}'.format(x, y, a))
    if op == '-':
        if x < y:
            t = x
            x = y
            y = t
            a = Fraction(x) - Fraction(y)
            a = real_fra(a)
            print(NUM, '. {} - {} ={}'.format(x, y, a))
    if op == '*':
        a = Fraction(x) * Fraction(y)
        real_fra(a)
        print(NUM, '. {} * {} ={}'.format(x, y, a))
    if op == '/':
        a = Fraction(x) / Fraction(y)
        real_fra(a)
        print(NUM, '.  {} / {} ={}'.format(x, y, a))


def Create_formula(serial):
    amount = int(serial[0:4])
    for i in range(0, amount):
        function()


# 主函数
if __name__ == "__main__":
    serial = ""
    quantity = Get_quantity()
    numrange = Get_range()
    serial = Add_num(numrange, serial, 3)
    serial = Add_num(quantity, serial, 4)
    # print(Create_integer(serial))
    # print(Create_fraction(serial))
    Create_formula(serial)
    Create_txt("Exercises", serial, 1)
    print("此次生成的序列号为:", serial)
