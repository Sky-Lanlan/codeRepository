 #strip(object) 参数默认为空格
s = "!!hello,world!!"
s1 = s.strip('!')
print(s1)

# string.join(seq) 连接字符串
str = "-"
seq = ("a", "b", "c")
print(str.join(seq)) 

# str.replace(old,new[,max]) 把字符串中的 old（旧字符串）
# 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
str = "hello,world"
print(str.replace("l","a",1))

# str.split(str[,num])通过指定分隔符对字符串进行切片，
# 如果参数num 有指定值，则仅分隔 num 个子字符串
str  = "a,b,c,d"
print(str.split(",",1))

# str.count(sub, start= 0,end=len(string))统计字符串里某
# 个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
str  = "you are beautiful!"
print(str.count("u",0,len(str)))