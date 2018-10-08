# coding=utf-8
from scipy import *
from math import log
import random


# 计算给定数据的香浓熵：
def calc_shannon_ent(data_set):
    num_entries = len(data_set)  # 数据总个数
    label_counts = {}  # 标签类别字典（类别的名称为键，该类别的个数为值）
    for featVec in data_set:
        current_label = featVec[-1]  # 选取最后一列，为标签列
        if current_label not in label_counts.keys():  # 还没添加到字典里的类型
            label_counts[current_label] = 0
        label_counts[current_label] += 1
    shannon_ent = 0.0
    for keys in label_counts:  # 求出每种类型的熵
        prob = float(label_counts[keys]) / num_entries  # 每种类型个数占所有的比值
        shannon_ent -= prob * log(prob, 2)
    return shannon_ent  # 返回熵


# 按照给定的特征划分数据集,剔除含选出属性的一列，lisan属性为true即为离散
def split_data_set(data_set, axis, value, flag, lisan=True):
    ret_data_set = []
    if lisan:
        # 按dataSet矩阵中的第axis列的值等于value的分数据集
        for featVec in data_set:
            # 值等于value的，每一行为新的列表（去除第axis个数据）
            if featVec[axis] == value:
                reduced_feat_vec = featVec[:axis]
                reduced_feat_vec.extend(featVec[axis + 1:])
                ret_data_set.append(reduced_feat_vec)
    else:
        for featVec in data_set:
            if flag:
                if featVec[axis] >= value:
                    reduced_feat_vec = featVec[:axis]
                    reduced_feat_vec.extend(featVec[axis + 1:])
                    ret_data_set.append(reduced_feat_vec)
            else:
                if featVec[axis] < value:
                    reduced_feat_vec = featVec[:axis]
                    reduced_feat_vec.extend(featVec[axis + 1:])
                    ret_data_set.append(reduced_feat_vec)
    return ret_data_set  # 返回分类后的新矩阵


# 选择最好的数据集划分方式
def choose_best_feature_to_split(data_set):
    num_features = len(data_set[0]) - 1  # 求属性的个数,减一是因为数据集里有结果那一列
    base_entropy = calc_shannon_ent(data_set)  # 计算 Ent(D) 计算纯度
    best_infoGain = 0.0  # 最大的信息增益
    best_feature = -1  # 选择出信息增益最大的列的下标
    for i in range(num_features):  # 求所有属性的信息增益
        feat_list = [example[i] for example in data_set]  # 获得第i列的值
        new_entropy = 0.0
        split_info = 0.0  # 属性的固有值，属性类别越多，值越大
        # 判断是否为离散属性
        if type(feat_list[0]) is float:  # 连续型
            flag = True  # 标记为连续型
            temp_list = list(set(sorted(feat_list)))  # 排序
            candidate = []  # 候选值
            # temp_list = list(set(temp_list))
            for j in range(len(temp_list) - 1):
                candidate.append((temp_list[j] + temp_list[j + 1]) / 2)  # 计算中位点
            unique_values = set(candidate)  # 所有候选值
            # 考察每一个候选值，选出最大信息熵所对应的候选值作为阈值
            infoGain = 0
            for value in unique_values:  # 求第i列属性每个不同值的熵*他们的概率
                # 获取只含小于value的样本集
                sub_data_set = split_data_set(data_set, i, value, 0, False)
                # 获取只含属性大于等于value的样本集
                sub_data_set1 = split_data_set(data_set, i, value, 1, False)
                prob_a = len(sub_data_set) / float(len(data_set))  # 求出该值在i列属性中的概率
                # 计算条件熵
                new_entropy = \
                    prob_a * calc_shannon_ent(sub_data_set) + (1 - prob_a) * calc_shannon_ent(sub_data_set1)
                sub_infoGain = (base_entropy - new_entropy)  # 求出第i列属性的信息增益
                if sub_infoGain > infoGain:  # 记录阈值信息
                    infoGain = sub_infoGain
                    if sub_infoGain > best_infoGain:
                        best_feature = [value, i]  # 我需要记录i值
        else:
            flag = False
            unique_values = set(feat_list)  # 第i列属性的取值（不同值）数集合
            for value in unique_values:  # 求第i列属性每个不同值的熵*他们的概率
                # 获取只含属性等于value的样本集
                sub_data_set = split_data_set(data_set, i, value, 0)
                # 求出该值在i列属性中的概率
                prob = len(sub_data_set) / float(len(data_set))
                if prob == 0 or prob == 1:
                    split_info = 1
                    break
                else:
                    # 求i列属性各值对应的熵求和
                    new_entropy += prob * calc_shannon_ent(sub_data_set)
                    split_info -= prob * log(prob, 2)
            # 求出第i列属性的信息增益率

            infoGain = (base_entropy - new_entropy) / split_info

            # 保存信息增益率最大的信息增益率值以及所在的下标（列下标i）
        if infoGain > best_infoGain:
            best_infoGain = infoGain
            if not flag:
                best_feature = i
    return best_feature


# 找出出现次数最多的分类名称
def majority_cnt(class_list):
    class_count = {}
    for vote in class_list:
        if vote not in class_count.keys():
            class_count[vote] = 0
        class_count[vote] += 1
    max_1 = 0
    for d in class_count:
        if max_1 < class_count.get(d):
            max_1 = class_count.get(d)
            result = d
    return result


# 创建树
def create_tree(data_set, labels_c):
    # 创建需要创建树的训练数据的结果列表
    class_list = [example[-1] for example in data_set]
    # 如果所有的训练数据都是属于一个类别，则返回该类别
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    # 训练数据只给出类别数据（没给任何属性值数据），返回出现次数最多的分类名称
    if len(data_set[0]) == 1:
        return majority_cnt(class_list)
    if len(data_set) <= 3:
        return majority_cnt(class_list)
    # 选择信息增益最大的属性进行分（返回值是属性类型列表的下标，连续型为节点值和下标）
    best_feat = choose_best_feature_to_split(data_set)

    # 剪枝操作
    if type(best_feat) == list:  # 为连续属性
        best_feat_label = labels_c[best_feat[1]]
        my_tree = {best_feat_label: {}}  # 以bestFeatLabel为根节点建一个空树
        del (labels_c[best_feat[1]])  # 从属性列表中删掉已经被选出来当根节点的属性
        key1 = "<" + str(best_feat[0])
        key2 = ">=" + str(best_feat[0])
        # 这里大概花了我两天的时间，因为python list递归会出现问题，
        # 所以需要复制操作 sub_labels = labels_c[:]
        sub_labels = labels_c[:]
        # split_data_set 函数 倒数第二个参数 1代表选中大于value的 0 代表小于
        return_tree1 = \
            create_tree(split_data_set(data_set, best_feat[1], best_feat[0], 0, False), sub_labels)
        sub_labels = labels_c[:]
        return_tree2 = \
            create_tree(split_data_set(data_set,best_feat[1], best_feat[0], 1, False), sub_labels)
        my_tree[best_feat_label][key1] = return_tree1  # 根据各个分支递归创建树
        my_tree[best_feat_label][key2] = return_tree2  # 根据各个分支递归创建树
    else:
        best_feat_label = labels_c[best_feat]  # 根据下表找属性名称当树的根节点
        my_tree = {best_feat_label: {}}  # 以bestFeatLabel为根节点建一个空树
        del (labels_c[best_feat])  # 从属性列表中删掉已经被选出来当根节点的属性
        # 找出该属性所有训练数据的值（创建列表）
        feat_values = [example[best_feat] for example in data_set]
        unique_values = set(feat_values)  # 求出该属性的所有值得集合（集合的元素不能重复）
        for value in unique_values:  # 根据该属性的值求树的各个分支
            sub_labels = labels_c[:]
            # 根据各个分支递归创建树
            my_tree[best_feat_label][value] = \
                create_tree(split_data_set(data_set, best_feat, value, 0), sub_labels)
    return my_tree  # 生成的树


# 实用决策树进行分类
def classify(input_tree, feat_labels, test_vec):

    global class_label
    first_str = str(input_tree.keys())[12:-3]  # 得到第一个字典的key
    second_dict = input_tree[first_str]
    feat_index = feat_labels.index(first_str)
    for key1 in second_dict.keys():
        if key1.count("<"):     # 连续
            key2 = float(key1[1:])
            if test_vec[feat_index] <= key2:
                if type(second_dict[key1]).__name__ == 'dict':  # 如果没有到最底层，递归
                    class_label = classify(second_dict[key1], feat_labels, test_vec)
                else:
                    class_label = second_dict[key1]
        elif key1.count(">="):
            key2 = float(key1[2:])
            if test_vec[feat_index] > key2:
                if type(second_dict[key1]).__name__ == 'dict':  # 如果没有到最底层，递归
                    class_label = classify(second_dict[key1], feat_labels, test_vec)
                else:
                    class_label = second_dict[key1]
        else:                                     # 离散
            if test_vec[feat_index] == key1:
                if type(second_dict[key1]).__name__ == 'dict':  # 如果没有到最底层，递归
                    class_label = classify(second_dict[key1], feat_labels, test_vec)
                else:
                    class_label = second_dict[key1]
    return class_label


# # 读取数据文档中的训练数据（生成二维列表）
# def create_train_data():
#     lines_set = open('E:\myCodes\python\mlTest\\venv\src\data\letter_train.txt').readlines()
#     data_x = []
#     for temp in lines_set:
#         # 将标签移至最后一列
#         temp2 = list(temp[:].split("\n")[0].split(","))
#         # print(temp2)
#         c = temp2[-1]
#         temp2[-1] = temp2[0]
#         temp2[0] = c
#         temp2 = list(map(float, temp2[:-1])) + temp2[-1:]
#         # print("##", temp2)
#         data_x.append(temp2)
#     label = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11',
#              'A12', 'A13', 'A14', 'A15', 'A16']
#     return data_x, label


# # 读取数据文档中的测试数据（生成二维列表）
# def create_test_data():
#     lines_set = open('E:\myCodes\python\mlTest\\ven'
#                      'v\src\data\letter_test.txt').readlines()
#     data_x = []
#     data_y = []
#     for temp in lines_set:
#         temp2 = list(temp[:].split("\n")[0].split(","))
#         c = temp2[-1]
#         temp2[-1] = temp2[0]
#         temp2[0] = c
#         temp3 = list(map(float, temp2[:-1]))
#         data_x.append(temp3)
#         data_y.append(temp2[-1:])
#     print(data_x, data_y)
#     return data_x, data_y


# 读取数据文档中的训练数据（生成二维列表）
def create_train_data(k):
    lines_set = open('E:\myCodes\python\mlTest\\venv\src\data\winequality-red.csv').readlines()
    data = []

    for temp in lines_set:
        temp2 = list(temp[:].split("\n")[0].split(";"))
        # c = temp2[-1]
        # temp2[-1] = temp2[0]
        # temp2[0] = c
        tmp = []
        for i in range(len(temp2)):
            if i != len(temp2) - 1:
                tmp.append(float(temp2[i]))
            else:
                tmp.append(temp2[i])
        data.append(tmp[:])
        # data.append(temp2)
    label = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11',
             ]
    list1 = list(range(0, len(data), k))
    w = random.sample(list1, 1)[0]
    data_x = []
    data_x.extend(data[:w])
    data_x.extend(data[w+int(len(data)/k):])
    test_y = [i[-1:]for i in data[w:w+int(len(data)/k)]]
    test_x = [i[:-1]for i in data[w:w+int(len(data)/k)]]
    return data_x, label, test_x, test_y


if __name__ == '__main__':
    k = 10
    avg_accuracy = 0

    for p in range(k):
        accuracy = 0
        my_dat_x, labels, test_list, test_labels = create_train_data(k)
        myTree = create_tree(my_dat_x, labels)
        # print(myTree)
        # 重新创建一次属性列表，具体原因尚不太明白
        boot_labels = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11',
             ]
        labels_num = {}
        total = len(test_labels)
        pre = []
        count = 0
        for testData in test_list:
            pre.append(classify(myTree, boot_labels, testData))
        for ic in range(total):
            key = set(test_labels[ic])
            labels_num[str(key)] = 1
            if pre[ic] == str(test_labels[ic])[2:-2]:
                count += 1
        accuracy = count / total * 100
        avg_accuracy += accuracy/k
        print("第", (p+1), "次测试准确率为：", accuracy, "%")
        if p == k-1:
            print("样本数量为：", len(my_dat_x))
            print("测试数量为：", len(test_list))
            print("属性类为：", len(my_dat_x[0])-1)
            print("标签结果：", len(labels_num))
            print("测试平均准确率为：", avg_accuracy, "%")
