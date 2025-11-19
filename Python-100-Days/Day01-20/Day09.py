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