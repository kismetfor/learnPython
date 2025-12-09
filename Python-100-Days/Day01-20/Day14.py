m = 7
n = 3
m1 = 1
for i in range(1, m+1):
    m1 *= i
n1 = 1
for i in range(1, n+1):
    n1 *= i
mn = 1
for i in range(1, m-n+1):
    mn *= i
res = m1/n1/mn
print(res)

def factorial(n):
    res = 1
    for i in range(1, n+1):
       res *= i
    return res

def Cmn(m, n):
    m1 = factorial(m)
    n1 = factorial(n)
    mn = factorial(m-n)
    # // 是整除法，返回整数；/返回 float，组合数一定是整数
    return m1//n1//mn

print(Cmn(7, 3))

"""
重复发明轮子”是一件非常糟糕的事情。
对于上面的代码，如果你觉得factorial这个名字太长，书写代码的时候不是特别方便，
我们在导入函数的时候还可以通过as关键字为其别名。在调用函数的时候，
我们可以用函数的别名，而不再使用它之前的名字，代码如下所示。

"""
from math import factorial as fac

print(fac(3))

"""
函数的参数
位置参数和关键字参数
我们再来写一个函数，根据给出的三条边的长度判断是否可以构成三角形，如果可以构成三角形则返回True，否则返回False，代码如下所示。
"""
def make_judgement(a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a+b>c and b+c>a and c+a>b
"""
上面make_judgement函数有三个参数，
这种参数叫做位置参数，在调用函数时通常按照从左到右的顺序依次传入，
而且传入参数的数量必须和定义函数时参数的数量相同，如下所示。
如果不想按照从左到右的顺序依次给出a、b、c 三个参数的值，也可以使用关键字参数，通过“参数名=参数值”的形式为函数传入参数，如下所示。
"""
make_judgement(a=1, b=2, c=3)
"""
在定义函数时，我们可以在参数列表中用/设置强制位置参数（positional-only arguments），
用*设置命名关键字参数。所谓强制位置参数，就是调用函数时只能按照参数位置来接收参数值的参数；
而命名关键字参数只能通过“参数名=参数值”的方式来传递和接收参数，大家可以看看下面的例子。
"""