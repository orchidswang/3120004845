
import jieba
from jieba import analyse
from line_profiler_pycharm import profile
import os
import re
from simhash import Simhash





@profile
def simhash_similarity(text1, text2):
    word1 = jieba.lcut(text1, cut_all=False, HMM=False)
    word2 = jieba.lcut(text2, cut_all=False, HMM=False)
    print(word1)
    print(word2)

    #将提取出来的关键词进行Simhash处理
    a_simhash = Simhash(word1)
    b_simhash = Simhash(word2)
    print("原论文的Simhash值:",a_simhash.value)
    print("疑似抄袭论文的Sinhash值:",b_simhash.value)

    #取得两个hash值中长度较大的作为参考长度
    hashbit = max(len(bin(a_simhash.value)),len(bin(b_simhash.value)))

    #计算两个hash值之间的汉明距
    distince = a_simhash.distance(b_simhash)
    print("两文章Simhash处理后的汉明距离为:", distince)
    distince1 = distince
    if(distince <= 5): distince1 = 0
    similar = (1-(distince / hashbit))*100 - distince1*1.8

    #如果两篇文章相似度不高,使用分词会导致相似度虚高,所以使用关键词提取来判断文本相似度
    '''if(similar<=80):
        word1 = analyse.extract_tags(text1, topK=800)
        word2 = analyse.extract_tags(text2, topK=800)
        a_simhash = Simhash(word1)
        b_simhash = Simhash(word2)
        distince = a_simhash.distance(b_simhash)
        print(distince)
        similar = (1-(distince / hashbit)) * 100 - distince'''

    return similar

#去除标点符号
def remove_punctuation(data):
    data1 = []
    remove_chars = '[·’!"\#$%&\'()＃！（）*+,-./:;<=>?\@，：?￥★、…．＞【】［］《》？“”‘’\[\\]^_`{|}~]+'
    string = re.sub(remove_chars, "", data)
    data1.append(string)
    return data1
@profile
def main():


    file1 = '测试文本/orig.txt'
    f1 = open(file1, encoding='utf-8')

    file2 = '测试文本/three bodies.txt'
    f2 = open(file2, encoding='utf-8')

    # 将原文文本导入到程序中去
    data1_notremove = f1.read()
    data1_ = remove_punctuation(data1_notremove)
    data1 = str(data1_)
    f1.close()


    # 将鉴定抄袭文本导入到程序中去
    data2_notremove =f2.read()
    data2_ = remove_punctuation(data2_notremove)
    data2 = str(data2_)
    f2.close()

    similary = simhash_similarity(data1, data2);
    print("论文原文的绝对路径:", os.path.abspath(file1))
    print("抄袭论文的绝对路径:", os.path.abspath(file2))
    print("文本相似度:", similary,"%")



#运行程序
main()
