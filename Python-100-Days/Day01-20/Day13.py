xinhua = {
    '麓': '山脚下',
    '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
    '蕗': '甘草的别名',
    '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}
print(xinhua)
person = {
    'name':'lihua',
    'age': 18,
    'num': '188918'
}
print(person)

"""
当然，如果愿意，我们也可以使用内置函数dict或者是字典的生成式语法来创建字典，代码如下所示。

"""
person = dict(name='lihua', age=18, num='188918')
print(person)
# 可以通过Python内置函数zip压缩两个序列并创建字典
list1 = [1, 2, 3]
list2 = [x**2 for x in list1]
print(list2)
items1 = dict(zip(list1, list2))
print(items1)
items2 = dict(zip('ABCDEF', range(1, 10)))
print(items2)
# 用字典生成式语法创建字典
items3 = {x: x**3+1 for x in range(1, 10)}
print(items3)

"""
字典的运算
字典中的键必须是不可变类型
"""