d={'a':1000,'b':1001,'c':1002,'d':1003}
d_b=d['b']
print(d_b)

print('x' in d)

d.get('x',10010)
print(d.get('x'))
print(d.get('x',10010))
print(d.get('a'))

'''
修改字典
向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
'''
d['a']='1000x'
print(d['a'])
d['e']=1004
print(d['e'])
'''
删除字典元素
能删单一的元素也能清空字典，清空只需一项操作。
'''
del d['a']
print(d['b'])

d.clear()

'''
set
'''
a=set([1,2,3])
b=set([3,4,5])
print(a)
a.add(4)
print(a)
a.remove(4)
print(a)
print(a & b)
print(a | b)
