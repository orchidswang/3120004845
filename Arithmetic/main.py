import time
from datetime import datetime
import datetime
import re



#删除字符串中的标点符号
def Remove_punctuation(data):
    data1 = []
    remove_chars = '[-./:;<=>?\@，：?￥★、…．＞【】［］《》？“”‘’\[\\]^_`{|}~]+'
    string = re.sub(remove_chars, "", data)
    data1.append(string)
    return data1

#通过当前时间生成hash的函数
def Generate_hash():
    now = str(datetime.datetime.now())
    now = str(Remove_punctuation(now))  # 去除时间中的多余的符号
    now = now.replace("[", "").replace("'", "").replace(" ", "").replace("'", "'").replace("]", "")  # 将空格与[]符号去除
    hash1 = hash(now)
    if hash1 < 0 : hash1 = -hash1
    return hash1

#连接两个数字的函数

def Stitching_Numbers(num1, num2):
    if (type(num1) == int): str1 = str(num1)
    if (type(num2) == int): str2 = str(num2)
    str3 = str1 + str2
    return str3

#创建序列号函数

def Get_serial_number():
    num1 = Generate_hash()
    time.sleep(0.2)  # 等待0.2s,以便于生成两个不同的哈希值
    num2 = Generate_hash()
    serial = Stitching_Numbers(num1, num2)
    return serial

#文件写入函数
def Create_txt(msg,model):
    if model == 1:  #模式1:创建txt文件以及序列号
        with open("Exercises.txt", "a+") as file1:
            file1.write(msg+"\n")
            file1.close()
    return 0

#在序列号中添加题目数量函数
def Add_num(quantity,serial):
    str1 = "0"
    str2 = ""
    if len(quantity) < 4:
        for i in range(0, 4 - len(quantity)):
            str2 += str1
    quantity = str2 + quantity
    serial = quantity + serial
    return serial



#获取生成题目数量的函数
def Get_quantity():
    #判断字符串是否大于5的函数
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


if __name__ == "__main__":
    serial = Get_serial_number()
    quantity = Get_quantity()
    serial = Add_num(quantity,serial)
    Create_txt(serial,1)
    print("此次生成的序列号为:", serial)
