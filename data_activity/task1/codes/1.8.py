# 列表
list = ['we',"us",2,3,4]
# 增加元素
list.append('Google')
print("增加元素之后：",list)

# 删除元素
del list[1]
print("删除元素之后：",list)

# 查找元素  当索引为负数时，表示从末尾开始查找
print(list[1:3])
print(list[1:])
print(list[-2])

# 元组
tup1 = ('physics','chemistry',1992,1996)
# 创建一个只含有一个元素的元组时，要在元素后面添加逗号
tup2 = (3,)
# 创建一个含有一个列表元素的元组
tup3 = (["lanlan",333],'lvlv')
tup3[0].append(222)
print(tup1)
print(tup2)
print(tup3)

tup = 2,3,4
print(type(tup))

# 字典
 
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
print(dict)
dict['Name'] = 'Lanlan'
print(dict)
del dict['Name']; # 删除键是'Name'的条目
dict.clear();     # 清空词典所有条目