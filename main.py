import jieba
import cProfile #, pstats, io
from line_profiler_pycharm import profile
import os
import re
from simhash import Simhash

pr = cProfile.Profile()
pr.enable()


@profile
def simhash_similarity(text1, text2):
    word1 = jieba.lcut(text1, cut_all=False, HMM=True)
    word2 = jieba.lcut(text2, cut_all=False, HMM=True)
    print(word1)
    print(word2)

    # 将提取出来的关键词进行Simhash处理
    a_simhash = Simhash(word1)
    b_simhash = Simhash(word2)
    print("原论文的Simhash值:", a_simhash.value)
    print("疑似抄袭论文的Sinhash值:", b_simhash.value)

    # 取得两个hash值中长度较大的作为参考长度
    hashbit = max(len(bin(a_simhash.value)), len(bin(b_simhash.value)))

    # 计算两个hash值之间的汉明距
    distince = a_simhash.distance(b_simhash)
    print("两文章Simhash处理后的汉明距离为:", distince)
    distince1 = distince
    # 因为汉明距大于10,就说明两篇文章相关性不大,于是在大于10时相似度要减掉2倍的汉明距,以降低其相似度
    if (distince <= 10): distince1 = 0
    similar = round((1 - (distince / hashbit)) * 100 - distince1 * 2, 2)

    return similar


# 去除标点符号
@profile
def remove_punctuation(data):
    data1 = []
    remove_chars = '[·’!"\#$%&\'()＃！（）*+,-./:;<=>?\@，：?￥★、…．＞【】［］《》？“”‘’\[\\]^_`{|}~]+'
    string = re.sub(remove_chars, "", data)
    data1.append(string)
    return data1


@profile
def main():
    file1 = '测试文本/ori.txt'
    file2 = '测试文本/ori_0.8_del.txt'

    # 判断文件是否存在,如果不存在,则结束运行
    if (os.path.exists(file1) == False | os.path.exists(file2) == False):
        print("文件不存在,请重新输入")
        return 0

    f1 = open(file1, encoding='utf-8')
    f2 = open(file2, encoding='utf-8')

    # 将原文文本去除标点符号后导入到程序中去
    data1 = str(remove_punctuation(f1.read()))
    # 将鉴定抄袭文本去除标点符号后导入到程序中去
    data2 = str(remove_punctuation(f2.read()))

    similary = simhash_similarity(data1, data2)

    f1.close()
    f2.close()

    print("论文原文的绝对路径:", os.path.abspath(file1))
    print("抄袭论文的绝对路径:", os.path.abspath(file2))
    print("文本相似度:", similary, "%")

# 运行程序
main()

'''pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats()
ps.print_stats()
print(s.getvalue())
pr.dump_stats("pipeline.prof")'''
