# map
s = [1,2,3,4,5]
f = lambda x:x*2
r = map(f,s)
print(type(r))
print(list(r))

# reduce
from functools import reduce
s = [1,2,3,4,5]
def add(x,y):
	return x+y
print(reduce(add,s))
def calc(x,y):
	return 10*x+y
print(reduce(calc, s))

# filter 
# 在一个list中，删掉偶数，只保留奇数，可以这么写：

def is_odd(n):
    return n % 2 == 1
	
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

from inspect import isgeneratorfunction 
# list
# Python内置的sorted()函数就可以对list进行排序：
list = [2, 1, 4, 3, 0]
print(sorted(list))

# sorted()函数也是一个高阶函数，它还可以接收一个key函数
# 来实现自定义的排序，例如按绝对值大小排序：

list2 = sorted([36, 5, -12, 9, -21], key=abs)
print(list2)