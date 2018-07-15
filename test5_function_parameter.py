'''
Created on 2018年7月15日

@author: Administrator
'''
'''
*******************************************
 位置参数
'''
def power_1(x):
    return x*x

print(power_1(5))

'''
******************************************
现在，如果我们要计算x3怎么办？可以再定义一个power3函数，但是如果要计算x4、x5……怎么办？我们不可能定义无限多个函数。

你也许想到了，可以把power(x)修改为power(x, n)，用来计算xn，说干就干：
'''
def power_2(x,n):
    result_power = 1
    count_i = 1
    if n >= 0:
        while count_i <= n:
            result_power = result_power * x
            count_i = count_i + 1
        print(result_power)
    else:
        print("the n is wrong")

        
power_2(3,3)   
power_2(3,-1)

'''
*************************************
默认参数

''' 
def enroll(name,gender,city = "beijing",age = 6):
    print("name :",name)
    print("gender:",gender)
    print("city:",city)
    print("age:",age)   
print(enroll("zdl", "f"))
print(enroll("zdl", "f","x",7))
print(enroll("zdl", "f",7))
print(enroll("zdl", "f",age = 7))


def add_end(L=[]):
    L.append('END')
    return L
print(add_end([1, 2, 3]))
print(add_end())
print(add_end())
print(add_end([2]))

def add_end_mod(L=None):
    if L is None:
        L = []
    L.append('end')
    return L
print(add_end_mod([1, 2, 3]))
print(add_end_mod())
print(add_end_mod())

'''
***********************************************
可变参数
'''
'''
调用的时候，需要先组装出一个list或tuple：
'''
def calc(number):
    sum_n=0
    for n in number:
        sum_n = sum_n + n
    return sum_n
print(calc([1,2,3]))
print(calc((1,2,3)))

'''
利用可变参数，可以简化函数调用方法
'''
def calc_1(*number):
    sum_n=0
    for n in number:
        sum_n = sum_n + n
    return sum_n
print(calc_1(1,2,3))
print(calc_1(1,2,3,4))

def calc_list(*number):
    sum_n=0
    for n in number:
        sum_n = sum_n + n
    return sum_n
num=[1,2,3]
print(calc_list(*num))
num=[1,2,3,4]
print(calc_list(*num))
