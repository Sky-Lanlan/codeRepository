import time;

# 获取当前时间
localtime = time.localtime(time.time())
print("本地时间为：",localtime)
# 获取时间戳
print(time.time())

#以struct_time元组为基础，获取格式化时间
print("本地时间为：",time.asctime(time.localtime()))

# 使用time.strftime(format[, t])函数格式化日期

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
print(time.strftime("%Y-%m-%d %H:%M:%S"))#默认当地时间

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

import calendar

cal = calendar.month(2018, 4)
print("以下输出2018年4月份的日历:")
print(cal)