"""
在 Python 中，列表是由一系元素按特定顺序构成的数据序列，
这就意味着如果我们定义一个列表类型的变量，可以用它来保存多个数据。
在 Python 中，可以使用[]字面量语法来定义列表，列表中的多个元素用逗号进行分隔，代码如下所示。
"""
item1 = [1,2,3,4,5]
print(item1)
"""
除此以外，还可以通过 Python 内置的list函数将其他序列变成列表。准确的说，list并不是一个普通的函数，它是创建列表对象的构造器，后面的课程会为大家介绍对象和构造器这些概念。
"""
item2 = list(range(1,6))
print(item2)
item3 = list("hello")
print(item3)

print(item1+item2)
print(item3+item2)

"""
我们可以使用*运算符实现列表的重复运算，*运算符会将列表元素重复指定的次数，我们在上面的代码中增加两行，如下所示。
"""
print(item1*3)

"""
我们可以使用in或not in运算符判断一个元素在不在列表中，我们在上面的代码代码中再增加两行，如下所示。
"""
print( 3 in item2)
print( 3 in item3)

"""
正向索引和反向索引
相当于一个数轴
"""
items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items8[0])
print(items8[-len(items8)]) #相当于 0-n
print(items8[-1])

"""
切片运算是形如[start:end:stride]的运算符
其中start代表访问列表元素的起始位置，end代表访问列表元素的终止位置（终止位置的元素无法访问），而stride则代表了跨度
简单的说就是位置的增量，比如我们访问的第一个元素在start位置，那么第二个元素就在start + stride位置，当然start + stride要小于end。
"""
print(items8[1:5:1])

"""
如果start值等于0，那么在使用切片运算符时可以将其省略；
如果end值等于N，N代表列表元素的个数，那么在使用切片运算符时可以将其省略；
如果end值等于-N-1（因为：论述方式 1：正向索引 end = N，那么可以省略，对应最后一个索引+1，那么反向索引，也应该是end = 的数，为最后一个索引-1）
如果stride值等于1，那么在使用切片运算符时也可以将其省略。所以，下面的代码跟上面的代码作用完全相同。

"""
items9 = ['a', 'b', 'c', 'd', 'e']
#个人感悟：
    #  x:y:z，z 代表的是打印的方向，z<0，从后往前；z>0，从前往后
print(items9[0:5:1]) #0:N:1

print(items9[-5:0:1])
# print(items9[-5:0:1])切片 a[start:end:step]  start=-5，end=0，为什么 start<end，但是有问题？
"""
原因：
items9[-5:5:1]  等价于items9[0:5:1]  ，那照这个源码，也等价于items9[-500000:5:1]
处理逻辑
if (start < 0)
    start += length;
if (start < 0)
    start = 0;
if (start > length)
    start = length;
    如果 start 是负数 → 加上 length 变成正索引
如果加完还小于 0 → 设为 0
如果大于列表长度 → 设为 length
"""


print(items9[-500000:5:1])
print(items9[-1:-5:-1]) #-1:-N:-1

"""
切片 a[start:end:step] 的核心逻辑是：
	•	如果 step > 0（正方向）
    ➜ start 必须 < end 才能得到元素
    ➜ 否则直接是空列表
	•	如果 step < 0（反方向）
➜ start 必须 > end
"""

"""
总结
讲到这里，我们可以用列表的知识来重构上面“掷色子统计每种点数出现次数”的代码。
"""
import random
count = [0]*6
for _ in range(100):
    # random.randint(a, b) == random.randrange(a, b+1)
    """
    randint 内部就是：
       def randint(self, a, b):
            return self.randrange(a, b+1)
    """
    face = random.randrange(1, 7)
    count[face-1] += 1

print(count)