import jieba
from jieba import analyse
from simhash import Simhash


def simhash_similarity(text1, text2):

    #使用jieba进行关键词提取
    word1 = analyse.textrank(text1, topK=800)
    word2 = analyse.textrank(text2, topK=800)
    print(word1)
    print(word2)

    #将提取出来的关键词进行Simhash处理
    a_simhash = Simhash(word1)
    b_simhash = Simhash(word2)
    print(a_simhash.value)
    print(b_simhash.value)

    #取得两个hash值中长度较大的作为参考长度
    hashbit = max(len(bin(a_simhash.value)),len(bin(b_simhash.value)))

    #计算两个hash值之间的汉明距
    distince = a_simhash.distance(b_simhash)
    print("两文章Simhash处理后的汉明距离为:", distince)
    similar = (1-(distince / hashbit))*100
    return similar


# 将原文文本导入到程序中去
f1 = open('测试文本/orig.txt', encoding='utf-8')
data1 = f1.read()

# 将鉴定抄袭文本导入到程序中去
f2 = open('测试文本/orig_0.8_dis_1.txt', encoding='utf-8')
data2 = f2.read()

similary = simhash_similarity(data1, data2);
print("文本相似度:", similary)

f1.close()
f2.close()
