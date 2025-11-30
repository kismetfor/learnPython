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
person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': ['成都市武侯区科华北路62号1栋101', '北京市西城区百万庄大街1号'],
    'car': {
        'brand': 'BMW X7',
        'maxSpeed': '250',
        'length': 5170,
        'width': 2000,
        'height': 1835,
        'displacement': 3.0
    }
}
print(person)

"""
字典的方法
字典类型的方法基本上都跟字典的键值对操作相关，
其中get方法可以通过键来获取对应的值。
跟索引运算不同的是，
get方法在字典中没有指定的键时不会产生异常，
而是返回None或指定的默认值，代码如下所示。
"""
person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.get('name'))
print(person.get('name1'))
print(person.get('sex', True))  # True
"""
如果需要获取字典中所有的键，可以使用 keys 方法；
如果需要获取字典中所有的值，可以使用 values 方法。
字典还有一个名为items的方法，它会将键和值组装成二元组，通过该方法来遍历字典中的元素也是非常方便的。
"""
print(person.keys())
print(person.values())

