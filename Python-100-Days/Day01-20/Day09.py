"""
常用数据结构之列表-2
列表类型的变量拥有很多方法可以帮助我们操作一个列表
假设我们有名为foos的列表，列表有名为bar的方法，那么使用列表方法的语法是：foos.bar()
这是一种通过对象引用调用对象方法的语法
"""

"""
添加和删除元素
列表是一种可变容器，可变容器指的是我们可以向容器中添加元素、可以从容器移除元素，也可以修改现有容器中的元素
"""
languages = ['Python', 'Java', 'C++']
languages.append('Java')
languages.insert(1, 'Swift')
print(languages)
"""
我们可以用列表的remove方法从列表中删除指定元素，需要注意的是，如果要删除的元素并不在列表中，会引发ValueError错误导致程序崩溃，
所以建议大家在删除元素时，先用之前讲过的成员运算做一个判断
"""
languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
if 'Java' in languages:
    languages.remove('Java')
if 'SQL' in languages:
    languages.remove('SQL')
if 'Swift' in languages:
    languages.remove('Swift')
languages.pop()
print(languages)
languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
languages.pop(2)
print(languages)
languages.clear()
print(languages)

"""
这里还有一个小问题，例如languages列表中有多个'Python'，
那么我们用languages.remove('Python')是删除所有的'Python'，
还是删除第一个'Python'，大家可以先猜一猜，然后再自己动手尝试一下。
"""
languages = ['Python','C', 'Python','C','Python','Python','Python','Python', 'Java', 'C++', 'JavaScript']
if 'Python' in languages:
    languages.remove('Python')
languages.remove('Python')
print(languages)

"""
用 Python 中的del关键字后面跟要删除的元素，这种做法跟使用pop方法指定索引删除元素没有实质性的区别，但后者会返回删除的元素，前者在性能上略优
因为del对应的底层字节码指令是DELETE_SUBSCR，而pop对应的底层字节码指令是CALL_METHOD和POP_TOP
"""
items = ['Python', 'Java', 'C++']
del items[2]
print(items)

"""
元素位置和频次
列表的index方法可以查找某个元素在列表中的索引位置，如果找不到指定的元素，index方法会引发ValueError错误

"""
items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.index('Python', 1))

"""
元素排序和反转
列表的sort操作可以实现列表元素的排序，而reverse操作可以实现元素的反转，代码如下所示。
"""
# items.sort()
# print(items)
items.sort(reverse=True)
print(items)

"""
列表生成式
"""
# 场景一：创建一个取值范围在1到99且能被3或者5整除的数字构成的列表。
items1 = []
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        items1.append(i)
print(items1)
items11 = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items11)

# 场景二：有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方。
nums = [1, 2, 3, 4, 5]
nums2 = [num**2 for num in nums]
print(nums2)

# 场景三： 有一个整数列表nums1，创建一个新的列表nums2，将nums1中大于50的元素放到nums2中。
nums1 = [1, 2, 3, 4, 5, 100, 101, 102, 103, 51, 52, 53]
nums2 = [num for num in nums1 if num > 50]
print(nums2)

"""
用列表生成式创建列表不仅代码简单优雅，而且性能上也优于使用for-in循环和append方法向空列表中追加元素的方式
那是因为 Python 解释器的字节码指令中有专门针对生成式的指令（LIST_APPEND指令）；
而for循环是通过方法调用（LOAD_METHOD和CALL_METHOD指令）的方式为列表添加元素，方法调用本身就是一个相对比较耗时的操作
"""

"""
嵌套列表
"""
import random
scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
print(scores[1][2])

scores = []
for i in range(5):
    temp = []
    for j in range(5):
        score = random.randrange(1, 100)
        temp.append(score)
    scores.append(temp)
print(scores)

scores = []
scores = [[random.randrange(1, 100) for _ in range(5)] for _ in range(5)]
print(scores)

"""
列表的应用
下面我们通过一个双色球随机选号的例子为大家讲解列表的应用。双色球是由中国福利彩票发行管理中心发售的乐透型彩票，
每注投注号码由6个红色球和1个蓝色球组成。
红色球号码从1到33中选择，蓝色球号码从1到16中选择。
每注需要选择6个红色球号码和1个蓝色球号码，如下所示。
下面，我们通过 Python 程序来生成一组随机号码。
"""
red_balls = list(range(1, 34))

