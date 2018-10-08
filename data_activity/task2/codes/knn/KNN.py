# coding=utf-8
import numpy as np
import random


def deal_with_res(k):
    lines_set = open('iris.data.txt').readlines()
    data = []
    for temp in lines_set:
        temp2 = list(temp[:].split("\n")[0].split(","))
        tmp = []
        for i in range(len(temp2)):
            if i != len(temp2) - 1:
                tmp.append(float(temp2[i]))
            else:
                tmp.append(temp2[i])
        data.append(tmp[:])
    list1 = list(range(0, len(data), k))
    w = random.sample(list1, 1)[0]
    data_x = []
    data_x.extend(data[:w])
    data_x.extend(data[w + int(len(data) / k):])
    data_y = [i[-1:] for i in data_x]
    data_x = [i[:-1] for i in data_x]
    test_y = [i[-1:] for i in data[w:w + int(len(data) / k)]]
    test_x = [i[:-1] for i in data[w:w + int(len(data) / k)]]
    return data_x, data_y, test_x, test_y


def calc(test_x, test_y, inputs, k):
    # 计算距离
    temp = [list_sub(temp, inputs) for temp in test_x]
    temp2 = np.sum(temp, axis=1)
    distance = np.ndarray.tolist(temp2 ** 0.5)
    # 返回排序后的索引值
    sorted_dist_indices = arg_sort(distance)
    class_count = {}
    # 选择k个最近邻
    for k in range(k):
        vote_labels = test_y[sorted_dist_indices[k][0]]
        temp = str(vote_labels)[2:-2]
        class_count[temp] = class_count.get(temp, 0) + 1
    max_count = 0
    # 找出出现次数最多的类别
    for k in class_count:
        if class_count.get(k) > max_count:
            max_count = class_count.get(k)
            max_key = k
    return max_key


def list_sub(a, b):

    a = list(map(float, a))

    b = list(map(float, b))
    return list(np.fabs(np.array(a) - np.array(b)))


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
        temp = str(vote_labels)[2:-2]
        class_count[temp] = class_count.get(temp, 0) + 1

    max_count = 0
    for c in class_count:
        if class_count.get(c) > max_count:
            max_count = class_count.get(c)
            max_key = c

    return max_key


def arg_sort(distance):
    return sorted(enumerate(distance), key=lambda x: x[1])


if __name__ == '__main__':
    # list1[0] list1[1] list1[2] list1[3]
    # 分别代表样本属性，样本标签，测试属性，测试标签
    p = 10
    K = 5
    avg_accuracy = 0
    for w in range(p):
        accuracy = 0
        list1 = deal_with_res(p)
        total = len(list1[2])
        count = 0
        for i in range(total):
            pridict = calc(list1[0], list1[1], list1[2][i], K)
            if pridict == "".join(list1[3][i]):
                count = count + 1
        lebal_count = set(j[0] for j in list1[1])
        accuracy = count / total * 100
        avg_accuracy += accuracy / p
        print("第", (w + 1), "次测试准确率为：", accuracy, "%")
        if w == p-1:
            print("样本数量为：", len(list1[0]))
            print("测试数量为：", len(list1[2]))
            print("属性类为：", len(list1[0][0]))
            print("标签结果：", len(lebal_count))
            print("K值为：", K)
            print("测试平均准确率为：", avg_accuracy, "%")
