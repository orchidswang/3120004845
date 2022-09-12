import jieba
from simhash import Simhash


#将原文文本导入到程序中去
f1 = open('测试文本/orig.txt', encoding='utf-8')
data1 = f1.read()
f1.close()


#将鉴定抄袭文本导入到程序中去
f2 = open('测试文本/orig_0.8_dis_10.txt', encoding='utf-8')
data2 = f2.read()
f2.close()

words1 = jieba.lcut(data1, cut_all=True)
words2 = jieba.lcut(data2, cut_all=True)

print(words1)
print(words2)

sim = Simhash(words1).distance(Simhash(words2))
R_border = 10
L_border = 5
print("文章相似程度(越小越相似,最小为0):",sim)
if(sim > R_border):
    print("这两篇文章毫无相似的地方")
if(L_border<=sim<=R_border):
    print("这两篇文章有可能存在抄袭")
if(0<=sim<L_border):
    print("这两篇文章一定存在抄袭")