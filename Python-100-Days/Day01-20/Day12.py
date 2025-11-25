"""
常用数据结构之集合
在学习了列表和元组之后，我们再来学习一种容器型的数据类型，
它的名字叫集合（set）。说到集合这个词大家一定不会陌生，在数学课本上就有这个概念。
如果我们把一定范围的、确定的、可以区别的事物当作一个整体来看待，那么这个整体就是集合，集合中的各个事物称为集合的元素。
通常，集合需要满足以下要求：
无序性：一个集合中，每个元素的地位都是相同的，元素之间是无序的。
互异性：一个集合中，任何两个元素都是不相同的，即元素在集合中只能出现一次。
确定性：给定一个集合和一个任意元素，该元素要么属这个集合，要么不属于这个集合，二者必居其一，不允许有模棱两可的情况出现。

"""
"""
创建集合
还可以使用生成式语法来创建集合，就像我们之前用生成式语法创建列表那样
"""
set1 = {1,2,3,4,3}
print(set1)
set2 = {'banana', 'pitaya', 'apple', 'apple', 'banana', 'grape'}
print(set2)
set3 = set('hello')
print(set3)
set4 = {num for num in range(1, 101) if num%2 != 0}
print(set4)
"""
要提醒大家，集合中的元素必须是hashable类型，
所谓hashable类型指的是能够计算出哈希码的数据类型，
通常不可变类型都是hashable类型，如整数（int）、浮点小数（float）、布尔值（bool）、字符串（str）、元组（tuple）等。
可变类型都不是hashable类型，因为可变类型无法计算出确定的哈希码

我们不能将列表作为集合中的元素；同理，由于集合本身也是可变类型，所以集合也不能作为集合中的元素。我们可以创建出嵌套列表（列表的元素也是列表），但是我们不能创建出嵌套的集合

"""

"""
元素的遍历
可以通过len函数来获得集合中有多少个元素，但是我们不能通过索引运算来遍历集合中的元素，因为集合元素并没有特定的顺序
"""
print(len(set4))
set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
for element in set1:
    print(element)

set1 = {11, 12, 13, 14, 15}
print(10 in set1)
print(11 not in set1)

"""
集合的二元运算主要指集合的交集、并集、差集、对称差等运算，这些运算可以通过运算符来实现，也可以通过集合类型的方法来实现，代码如下所示。

"""
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
print(set1.intersection(set2))
print(set1 & set2)
# 并集
print(set1 | set2)
print(set1.union(set2))
# 差集
print(set1 - set2)
print(set1.difference(set2))

# 对称差 (set1 ∪ set2) - (set1 ∩ set2)
print(set1 ^ set2)
print(set1.symmetric_difference(set2))
"""
需要说明的是，集合的二元运算还可以跟赋值运算一起构成复合赋值运算，
例如：set1 |= set2相当于set1 = set1 | set2，
跟|=作用相同的方法是update；set1 &= set2相当于set1 = set1 & set2，
跟&=作用相同的方法是intersection_update，代码如下所示
"""
# set1.update(set2)
set1 |=set2
print(set1)
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}
# set1 &= set2
set1.intersection_update(set2)
print(set1)

"""
比较运算
如果两个集合中的元素完全相同，那么==比较的结果就是True，否则就是False
如果集合A的任意一个元素都是集合B的元素，那么集合A称为集合B的子集

"""
set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = {5, 4, 3, 2, 1}

set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = {5, 4, 3, 2, 1}

# print(set1 < set2)   # 真子集
# print(set1 <= set2)  # 子集，可以相等
print(set1.issubset(set2))
print(set1.issuperset(set3))
print(set2.issuperset(set1))

"""
集合的方法
刚才我们说过，Python 中的集合是可变类型，我们可以通过集合的方法向集合添加元素或从集合中删除元素。


"""
set1 = {1, 10, 100}

# 添加元素
set1.add(100)
set1.add(1000)
set1.add(10000)
print(set1)
# 删除元素
set1.discard(100)
if 10 in set1:
    set1.remove(10)
print(set1)
# 清空元素
set1.clear()
print(set1)
"""
集合类型还有一个名为isdisjoint (是否相交)的方法可以判断两个集合有没有相同的元素
如果没有相同元素，该方法返回True，否则该方法返回False，代码如下所示。
"""
set1 = {'Java', 'Python', 'C++', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))
"""
Python 中还有一种不可变类型的集合，名字叫frozenset。
set跟frozenset的区别就如同list跟tuple的区别，
frozenset由于是不可变类型，能够计算出哈希码，因此它可以作为set中的元素。除了不能添加和删除元素，frozenset在其他方面跟set是一样的
"""
fset1 = frozenset(i for i in range(1, 10) if i*2 < 15)
print(fset1)