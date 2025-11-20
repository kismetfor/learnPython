"""
元组的定义和运算
元组和列表的不同之处在于，元组是不可变类型
"""

# 定义一个三元组
t1 = (35, 12, 98)
# 定义一个四元组
t2 = ('骆昊', 45, True, '四川成都')
# 查看变量的类型
print(type(t1))  # <class 'tuple'>
print(type(t2))  # <class 'tuple'>

# 查看元组中元素的数量
print(len(t1))  # 3
print(len(t2))  # 4
# 索引运算
print(t1[0])    # 35
print(t1[2])    # 98
print(t2[-1])   # 四川成都
# 切片运算
"""
sequence[start : end : step]
"""
print(t2[:2])   # ('骆昊', 43)
"""
    # t2[0 : 2 : 1]
	•	start 省略 → 默认为 0
	•	end = 2
	•	step 省略 → 默认为 1
"""
print(t2[::3])  # ('骆昊', '四川成都') t2[0 : len(t2) : 3]

for element in t2:
    print(element)
# 成员运算
print(12 in t1)         # True
print(99 in t1)         # False
print('Hao' not in t2)  # True

t3 = t1 + t2
print(t3)

"""
一个元组中如果有两个元素，我们就称之为二元组；一个元组中如果五个元素，我们就称之为五元组。
需要提醒大家注意的是，()表示空元组，但是如果元组中只有一个元素，需要加上一个逗号，否则()就不是代表元组的字面量语法，而是改变运算优先级的圆括号，
所以('hello', )和(100, )才是一元组，而('hello')和(100)只是字符串和整数。
"""
"""
打包和解包操作
当我们把多个用逗号分隔的值赋给一个变量时，多个值会打包成一个元组类型；当我们把一个元组赋值给多个变量时，元组会解包成多个值然后分别赋给对应的变量，如下面的代码所示。
"""
# 打包操作
a = 1, 10, 100
print(type(a))  # <class 'tuple'>
print(a)        # (1, 10, 100)
# 解包操作
i, j, k = a
print(i, j, k)

"""
在解包时，如果解包出来的元素个数和变量个数不对应，会引发ValueError异常，
错误信息为：too many values to unpack（解包的值太多）
或not enough values to unpack（解包的值不足）。
有一种解决变量个数少于元素的个数方法，就是使用星号表达式。通过星号表达式，我们可以让一个变量接收多个值，代码如下所示。
需要注意两点：首先，用星号表达式修饰的变量会变成一个列表，列表中有0个或多个元素；
其次，在解包语法中，星号表达式只能出现一次。

"""
a = 1, 10, 100, 1000
i, j, *k = a
print(i, j, k)
a = 1
b = 2
c = 3
a, b = b, a
a, b, c = b, c, a
print(a, b, c)

"""
元组和列表的比较
元组是不可变类型，不可变类型更适合多线程环境，因为它降低了并发访问变量的同步化开销。
元组是不可变类型，通常不可变类型在创建时间上优于对应的可变类型
"""
import timeit

print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))

infos = ('骆昊', 43, True, '四川成都')
# 将元组转换成列表
print(list(infos))  # ['骆昊', 43, True, '四川成都']

frts = ['apple', 'banana', 'orange']
# 将列表转换成元组
print(tuple(frts))  # ('apple', 'banana', 'orange')