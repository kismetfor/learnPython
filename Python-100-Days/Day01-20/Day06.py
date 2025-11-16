import time

# hello = 1
# for _ in range(10):
#     print(f"{hello = :.1f}")
#     hello += 1
#     time.sleep(1)
# 上面代码的输出操作和休眠操作都没有用到循环变量i，对于不需要用到循环变量的for-in循环结构，按照 Python 的编程惯例，我们通常把循环变量命名为_

"""
break和continue
"""
# total = 0
# i = 2
# while True:
#     total += i
#     i += 2
#     if i > 100:
#         break
# print(total)

total = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue
    total += i
print(total)