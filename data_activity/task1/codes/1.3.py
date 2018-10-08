 # 默认参数
def stu(name,age = 22,city = "chongqing"):
	print(name,age,city)
	
# stu("lanlan")


# 不定长参数
def functionname(*var_args_tuple ):
	for var in var_args_tuple:
		print(var)

functionname(1,5,9)

# 匿名函数
s = lambda x:x*9
print(s(2))
