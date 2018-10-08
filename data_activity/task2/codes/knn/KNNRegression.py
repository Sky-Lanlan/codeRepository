# coding=utf-8
import numpy as np
import csv


def deal_with_res():
    csv_file = csv.reader(open('E:\myCodes\python\mlTest'
                               '\\venv\src\data\winequality-red.csv', 'r'))
    input_x = []
    input_y = []
    for stu in csv_file:
        slice1 = slice(11)
        slice2 = slice(11, 12)
        temp3 = stu[0].split(";")
        temp4 = [float(i) for i in temp3[slice1]]
        temp5 = [float(i) for i in temp3[slice2]]
        input_x.append(temp4)
        input_y.append(temp5)

    i = int(len(input_x)*2/3)
    slice3 = slice(i)
    slice4 = slice(i, len(input_x))
    train_x = input_x[slice3]
    train_y = input_y[slice3]
    test_x = input_x[slice4]
    test_y = input_y[slice4]
    y = lambda x: [(q - min(x)) / (max(x) - min(x)) for q in x]
    return list(map(y, train_x)), train_y, list(map(y, test_x)), test_y


def list_sub(a, b):
    result = np.array(a)-np.array(b)
    return list(np.fabs(result))


def calc(test_x, test_y, inputs, k):
    # 计算距离
    temp = [list_sub(temp, inputs) for temp in test_x]
    temp2 = np.sum(temp, axis=1)

    distance = np.ndarray.tolist(temp2 ** 0.5)
    # 返回排序后的索引值
    sorted_dist_indices = arg_sort(distance)
    class_count = {}
    # 选择k个最近邻
    for a in range(k):
        vote_labels = test_y[sorted_dist_indices[a][0]]
        temp = str(vote_labels)[1:-1]
        class_count[temp] = class_count.get(temp, 0) + 1
    sums = 0
    for c in class_count:
         sums = sums + class_count.get(c) * float(c)
    avg = sums/k
    return avg


def arg_sort(distance):
    return sorted(enumerate(distance), key=lambda x: x[1])


if __name__ == '__main__':
    # list1[0] list1[1] list1[2] list1[3]
    # 分别代表样本属性，样本标签，测试属性，测试标签
    K = 5
    list1 = deal_with_res()
    total = len(list1[2])
    entrpy = 0
    for o in range(total):
        pridict = calc(list1[0], list1[1], list1[2][o], K)
        entrpy = entrpy + abs(float(str(list1[3][o])[1:-1]) - pridict)
        print(o / total * 100, "%")
    print("样本数量为：", len(list1[0]))
    print("测试数量为：", len(list1[2]))
    print("属性类为：", len(list1[0][0]))
    print("K值为：", K)
    print("总cost为：", entrpy)