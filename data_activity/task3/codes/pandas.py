# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# a = pd.Series([1, 3, 4, 6])
# b = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
# c = pd.Series(np.random.randn(5),index=['a','b','c','d','f'])
# print(a[:3])
# s = b[b>b.median()]
# =============================================================================


# =============================================================================
# b = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
# print(b[[3,4]])
# print('默认索引：',a)
# print('创建索引：',b)
# =============================================================================

# =============================================================================
# print(b['b'])
# b['b'] = 13
# print(b)
# print(b.get('br'))
# =============================================================================


# =============================================================================
# # 使用dropna
# b = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
# c = pd.Series(np.random.randn(5),index=['a','b','c','d','f'])
# print('b*2:\n', b*2)
# print('b+b:\n', b+b)
# print('b+c:\n',b+c)
# print('使用dropna函数后：\n',(b+c).dropna())
# =============================================================================


# =============================================================================
# s = pd.Series(np.random.randn(5),name='something')
# print(s)
# print(s.name)
# 
# s2 = s.rename('different')
# s2[2] = 10
# print(s2)
# =============================================================================

# =============================================================================
# s = {'one':pd.Series(np.random.randn(5), index=['a','b','c','d','e']),
#                 'two':pd.Series(np.random.randn(3), index=['c','d','e'])}
# print('通过dict建立,无索引\n',pd.DataFrame(s))
# print('通过dict建立\n',pd.DataFrame(s,index=['e','d','c','b','a']))
# print('通过dict建立,指定行、列\n',pd.DataFrame(s,index=['e','b'],
#                                       columns=['two','three']))
# =============================================================================

# =============================================================================
# s = {'one':{'a':2,'b':4},
#      'two':{'a':4.,'b':6}}
# df = pd.DataFrame(s)
# print(df)
# df.index.name='row'
# df.columns.name='columns'
# print(df)
# print(df.values)
# print('使用序号索引row\n',df.iloc[1])
# print('使用key索引row\n',df.loc['a'])
# print('使用key索引columns\n',df['one'])
# print('使用key索引columns\n',df.one)
# print('位置索引',df.iat[1,1])
# =============================================================================

# =============================================================================
# print("原始数据")
# print(df)
# df['three'] = pd.Series([9,10],index=['a','b'])
# print("添加columns后")
# print(df)
# df.loc['c'] = pd.Series([11,11,14],index=['one','two','three'])
# print("添加row后")
# print(df)
# =============================================================================

# =============================================================================
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
#      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
#      'three' : pd.Series([10,20,30], index=['a','b','c'])}
# 
# df = pd.DataFrame(d,columns=['one','two','three'])
# df.index.name='row'
# print(df.axes)
# print("原始数据")
# print(df)
# del df['one']
# print("删除 one columns后")
# print(df)
# print("删除 a row后")
# print(df.drop('a'))
# =============================================================================

# =============================================================================
# s = pd.Series(np.random.randint(8,size=[3],dtype='int64'), 
#               index=['a','b','c'])
# print(s.axes)
# print(s.dtype)
# print(s.empty)
# print(s.size)
# print(s.values)
# print(s.head(2))
# print(s.tail(2))
# 
# =============================================================================


# =============================================================================
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
#    'Lee','David','Gasper','Betina','Andres']),
#    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
# df = pd.DataFrame(d)
# print(df)
# print('sum')
# print('axis=0')
# print(df.sum(0))
# print('axis=1')
# print(df.sum(1))
# print(df.describe())
# =============================================================================

# =============================================================================
# def adder(ele1,ele2):
#     return ele1+ele2
# 
# df = pd.DataFrame([[1,2,3],
#                    [3,4,5]],index=['a','b'],columns=['one','two','three'])
# =============================================================================
# =============================================================================
# print(df.apply(np.sum,1))
# =============================================================================

# =============================================================================
# s = pd.Series(np.random.randn(5))
# print(s)
# print(s.apply(np.mean,0))
# =============================================================================
# =============================================================================
# print(df)
# print('applymap')
# print(df.applymap(lambda x: x+3))
# print('pipe')
# print(df.pipe(lambda x: x+3))
# =============================================================================
# =============================================================================
# print('axis=1')
# print(df.apply(lambda x: x.max() - x.min(),1))
# =============================================================================

# =============================================================================
# print(df.one)
# =============================================================================

# =============================================================================
# df = pd.DataFrame(np.random.randn(10, 4))
# pieces = [df[:3], df[3:7], df[7:]]
# print('分割')
# print(pieces)
# print('拼接')
# print(pd.concat(pieces))
# =============================================================================

# =============================================================================
# left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
# right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
# print(left)
# print(right)
# print('连接后')
# print(pd.merge(left, right, on='key'))
# =============================================================================
# =============================================================================
# rng = pd.date_range('1/1/2012', periods=5, freq='S')
# ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
# print(ts)
# 
# print(ts.resample('5Min').sum())
# =============================================================================

# =============================================================================
# rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
# ts = pd.Series(np.random.randn(len(rng)), rng)
# print(ts)
# ts_utc = ts.tz_localize('UTC')
# print(ts_utc)
# print(ts_utc.tz_convert('US/Eastern'))
# =============================================================================

# =============================================================================
# df = pd.DataFrame({"id":[1,2,3,4,5,6], 
#                    "raw_grade":['a', 'b', 'c', 'a', 'a', 'e']})
# print(df)
# df["grade"] = df["raw_grade"].astype("category")
# print(df["grade"])
# 
# df["grade"].cat.categories = ["very good", "good","medium", "very bad"]
# print(df["grade"])
# =============================================================================




# =============================================================================
# ts = pd.Series(np.random.randn(1000), 
#                index=pd.date_range('1/1/2000', periods=1000))
# ts = ts.cumsum()
# ts.plot()
# 
# df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
#                       columns=['A', 'B', 'C', 'D'])
# df = df.cumsum()
# plt.figure()
# df.plot()
# plt.legend(loc='best')
# =============================================================================

# =============================================================================
# df = pd.DataFrame(np.random.randn(5,2),columns=['A', 'B'])
# df.to_csv('foo.csv')
# data = pd.read_csv('foo.csv')
# print(data)
# =============================================================================

# =============================================================================
# df = pd.DataFrame(np.random.randn(5,2),columns=['A', 'B'])
# df.to_hdf('foo.h5','df')
# data = pd.read_hdf('foo.h5','df')
# print(data)
# =============================================================================

# =============================================================================
# df = pd.DataFrame(np.random.randn(5,2),columns=['A', 'B'])
# df.to_excel('foo.xlsx', sheet_name='Sheet1')
# data = pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
# print(data)
# =============================================================================



s = pd.Series([False, True, False])
if  s.any():
    print('I am true')















