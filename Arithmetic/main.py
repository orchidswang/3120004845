import profile
import time
from datetime import datetime
import datetime
import re


def remove_punctuation(data):
    data1 = []
    remove_chars = '[-./:;<=>?\@，：?￥★、…．＞【】［］《》？“”‘’\[\\]^_`{|}~]+'
    string = re.sub(remove_chars, "", data)
    data1.append(string)
    return data1


def Generate_hash():
    now = str(datetime.datetime.now())
    now = str(remove_punctuation(now))  #去除时间中的多余的符号
    now = now.replace("[","").replace("'","").replace(" ","").replace("'","'").replace("]","")  #将空格与[]符号去除
    hash1 = hash(now)
    if (hash1<0): hash1 = -hash1
    return hash1


def Stitching_Numbers(num1,num2):
    if(type(num1) == int): str1 = str(num1)
    if(type(num2) == int): str2 = str(num2)
    str3 = str1+str2
    return str3


def get_serial_number():
    num1 = Generate_hash()
    time.sleep(0.2) #等待0.2s,以便于生成两个不同的哈希值
    num2 = Generate_hash()
    serial = Stitching_Numbers(num1,num2)
    print(serial)

def Generate_txt(str):
    return 0

get_serial_number()
quantity = input("请输入题目的数量:")







