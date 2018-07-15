a=['a','b','c']
for x in a:
    print(x)

sum=0
a=[1,2,3,4,5]
for x in a:
    sum=sum+x
print(sum)

sum=0
a=list(range(6))
for x in a:
    sum=sum+x
print(sum)


'''100以内，奇数之和'''
sum=0
a=1
while a < 100:
    sum = sum+a
    a=a+2
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
    
'''本来要循环打印1～100的数字,当n = 11时退出循环'''
a=1
while a < 101:
    print(a)
    a = a+1
    if a >=11:
        break

'''打印出1～10。但是，如果我们想只打印奇数，可以用continue语句跳过某些循环：'''

a=1
while a < 101:
    print(a)
    a = a+2
    if a >= 11:
        break


    
