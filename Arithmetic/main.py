import random
from fraction import Fraction
from random import choice
import os
from line_profiler_pycharm import profile

# 设置全局变量
NUM = 0


# 文件写入函数
@profile
def Create_txt(name, msg, model):
    if model == 1:  # 模式1:追加文本
        name = name + ".txt"
        with open(name, "a+") as file1:
            file1.write(msg + "\n")
            file1.close()
    if model == 2:  # 模式2:创建txt文件以及序列号
        name = name + ".txt"
        with open(name, "w+") as file1:
            file1.write(msg + "\n")
            file1.close()

    return 0


# 在序列号中添加题目数量函数
@profile
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
@profile
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
@profile
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
@profile
def Create_integer(serial):
    numrange = int(serial[4:7])
    intrger = random.randint(1, numrange)
    return intrger


# 生成分数的函数
@profile
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
@profile
def num_choice(serial):
    list1 = [Create_fraction(serial), Create_integer(serial)]
    return choice(list1)


# 选择运算符
@profile
def op_choice():
    list2 = ['+', '-', '*', '/']
    return choice(list2)


# 分数化简为整数/带分数
@profile
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
@profile
def function(serial):
    global NUM
    NUM = NUM + 1
    x = num_choice(serial)
    y = num_choice(serial)
    op = op_choice()

    if op == '+':
        a = Fraction(x) + Fraction(y)
        a = real_fra(a)
        str1 = str(NUM) + ". " + str(x) + " + " + str(y) + " =" + str(a)
        str2 = str(NUM) + ". " + str(x) + " + " + str(y) + " ="
        print(str1)
        Create_txt("answer", str1, 1)
        Create_txt("Exercises", str2, 1)
    if op == '-':
        if x < y:
            t = x
            x = y
            y = t
        a = Fraction(x) - Fraction(y)
        a = real_fra(a)
        str1 = str(NUM) + ". " + str(x) + " - " + str(y) + " =" + str(a)
        str2 = str(NUM) + ". " + str(x) + " - " + str(y) + " ="
        print(str1)
        Create_txt("answer", str1, 1)
        Create_txt("Exercises", str2, 1)
    if op == '*':
        a = Fraction(x) * Fraction(y)
        a = real_fra(a)
        str1 = str(NUM) + ". " + str(x) + " * " + str(y) + " =" + str(a)
        str2 = str(NUM) + ". " + str(x) + " * " + str(y) + " ="
        print(str1)
        Create_txt("answer", str1, 1)
        Create_txt("Exercises", str2, 1)
    if op == '/':
        a = Fraction(x) / Fraction(y)
        a = real_fra(a)
        str1 = str(NUM) + ". " + str(x) + " / " + str(y) + " =" + str(a)
        str2 = str(NUM) + ". " + str(x) + " / " + str(y) + " ="
        print(str1)
        Create_txt("answer", str1, 1)
        Create_txt("Exercises", str2, 1)


# 生成题目
@profile
def Create_formula(serial):
    amount = int(serial[0:4])
    for i in range(0, amount):
        function(serial)


# 生成题目文件
@profile
def Create_problems():
    serial = ""
    quantity = Get_quantity()
    numrange = Get_range()
    serial = Add_num(numrange, serial, 3)
    serial = Add_num(quantity, serial, 4)
    Create_txt("Exercises", serial, 2)
    Create_txt("answer", serial, 2)
    Create_formula(serial)
    print(quantity, "道四则运算已经生成完成,请在程序目录下查看生成的txt文件")


# 判断题目对错
@profile
def judge():
    answer = "answer.txt"
    exercises = "Exercises.txt"
    # 判断文件是否存在,如果不存在,则结束运行
    if (os.path.exists(answer) == False | os.path.exists(exercises) == False):
        print("文件不存在,请先生成题目!\n")
        return 0
    file1 = open(answer, "r")
    file2 = open(exercises, "r")
    Correctnum = 0
    Wrongnum = 0
    str1 = "("
    str2 = "("
    line = file1.readline()
    line_ = file2.readline()
    num = int(line[0:4])

    for i in range(0, num):
        line1 = file1.readline().strip()
        line2 = file2.readline().strip()
        if line1 == line2:
            Correctnum += 1
            bit = 1
            while line1[0:bit].isnumeric() == True:
                bit += 1
            str1 = str1 + line1[0:bit - 1] + ","
        else:
            Wrongnum += 1
            bit = 1
            while line2[0:bit].isnumeric() == True:
                bit += 1
            str2 = str2 + line1[0:bit - 1] + ","
    file1.close()
    file2.close()
    str1 = "Correct: " + str(Correctnum) + " " + str1 + ")"
    str2 = "Wrong: " + str(Wrongnum) + " " + str2 + ")"
    Create_txt("result", str1, 2)
    Create_txt("result", str2, 1)
    print(str1)
    print(str2)


# 主要程序
@profile
def run():
    while True:
        state = input("请输入你想要的功能:\n1生成题目  2对照答案 3退出程序\n")

        def judgenum(State):
            if State == "1" or State == "2" or State == "3":
                return True
            else:
                return False

        while judgenum(state) == False:
            state = input("输出错误!请重新输入:")

        if state == "1":
            Create_problems()
        if state == "2":
            judge()
        if state == "3":
            return 0


# 主函数
if __name__ == "__main__":
    run()
