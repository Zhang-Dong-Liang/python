'''
请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
'''
print(str(hex(10)))

def my_abs(x):
    if x <= 0:
        return -x
    else:
        return x

print(my_abs(-99))

'''
练习

请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

ax2 + bx + c = 0

的两个解。

提示：计算平方根可以调用math.sqrt()函数：

'''
import math
def quadratic(a,b,c):
    x1=(-b+(math.sqrt(b*b-4*a*c)))/(2*a)
    x2=(-b-(math.sqrt(b*b-4*a*c)))/(2*a)
    return x1,x2

print(quadratic(2,3,1))
