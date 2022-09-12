import jieba
from simhash import Simhash


#将原文文本导入到程序中去
f1 = open('测试文本/orig.txt', encoding='utf-8')
data1 = f1.read()
f1.close()


#将鉴定抄袭文本导入到程序中去
f2 = open('测试文本/three bodies.txt', encoding='utf-8')
data2 = f2.read()
f2.close()

words1 = jieba.lcut(data1, cut_all=False)
words2 = jieba.lcut(data2, cut_all=False)

print(words1)
print(words2)

print("文章相似程度(越小越相似,最小为0):",Simhash(words1).distance(Simhash(words2)))

