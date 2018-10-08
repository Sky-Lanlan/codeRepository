# 建立一个生成器
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

it = _odd_iter()

print(isgeneratorfunction(_odd_iter))
print(it.__next__())
print(it.__next__())
print(it.__next__())
