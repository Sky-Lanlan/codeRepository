import copy
from math import log
import random


# 定义一个标签类，用于存储标签信息
class Lable(object):
    def setValue(self, value):
        self.value = value

    def setIdx_list(self, idx_list):
        self.idx_list = idx_list

    def setCount(self, count):
        self.count = count


# 读取数据文档中的训练数据（生成二维列表）
def load_train_data(k):
    lines_set = open('PhishingData.arff.txt').readlines()
    data = []
    for temp in lines_set:
        temp2 = list(temp[:].split("\n")[0].split(","))
        # c = temp2[-1]
        # temp2[-1] = temp2[0]
        # temp2[0] = c
        data.append(temp2[:])
    list1 = list(range(0, len(data), k))
    w = random.sample(list1, 1)[0]
    data_x = []
    data_x.extend(data[:w])
    data_x.extend(data[w + int(len(data) / k):])
    data_y = [str(i[-1:])[2:-2] for i in data_x]
    data_x = [i[:-1] for i in data_x]
    test_y = [str(i[-1:])[2:-2] for i in data[w:w +
                                                int(len(data) / k)]]
    test_x = [i[:-1] for i in data[w:w + int(len(data) / k)]]
    return data_x, data_y, test_x, test_y


def init_table(data_set, lables):
    n = len(data_set)
    lab_list = []
    lab_set = set(lables)
    # 向标签类存数据
    for lab in lab_set:
        new_lab = Lable()
        new_lab.setValue(lab)
        count = 0
        sub_lab_list = []
        for index_lab in range(n):
            if lables[index_lab] == lab:
                count += 1
                sub_lab_list.append(index_lab)
        new_lab.setCount(count)
        new_lab.setIdx_list(sub_lab_list)
        lab_list.append(new_lab)
    list_resu = []
    # 遍历每个属性
    for i in range(len(data_set[0])):
        attra_i = []  # 存放所有样本在第i个属性的所有值
        # 遍历某个属性的所有样本
        for j in range(n):
            attra_i.append(data_set[j][i])  # j行，i列
        unique_att = set(attra_i)
        dic_att = {}

        for att in unique_att:
            dic_value = {}  # 存放属性值att所对应所有标签的样本个数

            # 遍历每个标签
            for item in lab_list:
                lable = item.value  # value即是标签
                for inner in item.idx_list:
                    if data_set[inner][i] == att:
                        if lable not in dic_value.keys():
                            dic_value[lable] = 0
                        dic_value[lable] += 1

                # 根据计数结果计算概率
                if lable in dic_value.keys():
                    dic_value[lable] = \
                     (dic_value[lable] + 1) / (item.count + len(unique_att))
            # 将未出现的属性处理
            for la in lab_set:

                if la not in dic_value.keys():
                    dic_value[la] = 1 / len(data_set)
            dic_att[att] = copy.deepcopy(dic_value)
        list_resu.append(copy.deepcopy(dic_att))
    return list_resu


def native_bayes(test_data, table_prob):
    n = len(test_data)
    list2 = []  # 存放结果
    list_tmp = []
    list_prob = []  # 存放每一个样本对应每个标签的概率的集合
    for item in range(n):
        # 第i个属性， 逐个计算每一个属性对应的概率
        for i in range(len(test_data[0])):
            value = test_data[item][i]  # 代表第item行，i列的值
            list_prob.append(table_prob[i][value])
        dic_line = {}
        for sub_pro in list_prob:
            for ree in sub_pro:
                if ree not in dic_line.keys():
                    dic_line[ree] = 1
                tmp = log(sub_pro[ree], 2)
                dic_line[ree] += tmp
        list_tmp.append(dic_line)
    for item in list_tmp:
        max_prob = float('-inf')
        max_key = ''
        for dic_item in item:
            if max_prob < item[dic_item]:
                max_prob = item[dic_item]
                max_key = dic_item
        list2.append(max_key)
    return list2


if __name__ == '__main__':
    K = 10
    avg_accuracy = 0
    for i in range(K):
        count = 0
        data_set, lables, test_set, test_lables =\
            load_train_data(K)
        labels_num = set(lables)
        total = len(test_lables)
        table_prob = init_table(data_set, lables)
        predict = native_bayes(test_set, table_prob)
        for j in range(len(test_set)):
            if predict[j] == test_lables[j]:
                count += 1
        accuracy = count / total * 100
        print("第", (i + 1), "次测试准确率为：", accuracy, "%")
        avg_accuracy += accuracy / K
        if i == K-1:
            print("样本数量为：", len(data_set))
            print("测试数量为：", len(test_set))
            print("属性类为：", len(data_set[0]))
            print("标签结果：", len(labels_num))
            print("测试平均准确率为：", avg_accuracy, "%")

