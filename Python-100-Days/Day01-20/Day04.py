# a = 10
# b = 3
# a += b        # 相当于：a = a + b
# a *= a + 2    # 相当于：a = a * (a + 2)
# print(a)      # 大家算一下这里会输出什么，我觉得是 13*15=169+26=195

"""
海象运算符
"""
# SyntaxError: invalid syntax
# print((a = 10))
# 海象运算符
# print((a := 10))  # 10
# print(a)          # 10

"""
例子1：华氏温度转摄氏温度
要求：输入华氏温度将其转换为摄氏温度，华氏温度到摄氏温度的转换公式为： 
C=(F−32)/1.8
"""
# f = float(input("请输入华氏度"))
# c = (f-32)/1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))
# print('%.1f' % f)
"""
关于占位符：
	•	%d —— 来自 decimal integer（十进制整数），所以对应 int
	•	%f —— 来自 floating-point number（浮点数），所以对应 float
	•	%s —— 来自 string（字符串），所以对应 str

"""
import math
"""
例子2：计算圆的周长和面积
要求：输入一个圆的半径（$\small{r}$），计算出它的周长（2πr）和面积（πr2）。
"""
# r = float(input("请输入半径 r"))
# perimeter = 2*math.pi*r
# area = math.pi*r*r
# print(f"周长perimeter = {perimeter:.2f}")
# print(f"面积area = {area:.2f}")

"""
例子3：判断闰年 
要求：输入一个 1582 年以后的年份，判断该年份是不是闰年。
"""
# year = int(input("年份："))
# print(year%4==0 and year % 100 != 0 or year % 400 == 0)