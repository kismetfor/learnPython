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