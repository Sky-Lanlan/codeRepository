# coding=utf-8
import numpy as np
import random


def distant_calc(centre, data_set):
    return np.sqrt(np.sum(np.power(centre - data_set, 2)))


def create_test_data():
    lines_set = open('winequality-red.csv').readlines()
    data_x = []
    data_y = []
    for data in lines_set:
        temp = data.split("\n")[0].split(";")
        tmp = list(map(float, temp[:-1]))
        max_c = max(tmp)
        min_c = min(tmp)
        tmp = [(i - min_c) / (max_c - min_c)for i in tmp]
        data_x.append(tmp)
        c = str(temp[-1:])[2:-2]
        data_y.append(c)
    print(data_x)
    return data_x, data_y


# 初始化聚簇中心，选取K个
def init_centre(data_set, k):
    n = np.shape(data_set)[1]
    centre = np.mat(np.zeros((k, n)))
    # print(np.shape(data_set)[0])
    r = random.sample(list(range(np.shape(data_set)[0])), k)
    print('初始化簇中心', r)
    # 随机选四个数据
    for row in range(k):
        centre[row] = data_set[r[row]]
    return centre


def k_means(dataSet, k, distMeans =distant_calc, createCent = init_centre):
    m = np.shape(dataSet)[0]  # 获取数据个数
    # cluster_infor第一列存放该数据所属的中心点，第二列是该数据到中心点的距离
    cluster_infor = np.mat(np.zeros((m, 2)))  # 用于存放该样本属于哪类及质心距离
    # print(data_set)
    centroids = createCent(dataSet, k)  # 初始化类簇
    cluster_changed = True  # 用来判断聚类是否已经收敛
    while cluster_changed:
        cluster_changed = False
        for i in range(m):  # 把每一个数据点划分到离它最近的中心点
            min_dist = float('inf')
            min_index = -1
            for j in range(k):
                distJI = distMeans(centroids[j], np.mat(dataSet[i]))
                if distJI < min_dist:
                    min_dist = distJI
                    # 如果第i个数据点到第j个中心点更近，则将i归属为j
                    min_index = j
            if cluster_infor[i, 0] != min_index:
                cluster_changed = True  # 如果分配发生变化，则需要继续迭代
                # 并将第i个数据点的分配情况存入字典
            cluster_infor[i, :] = min_index, min_dist
        for cent in range(k):  # 重新计算中心点
            # 去第一列等于cent的所有列
            new_clust = dataSet[np.nonzero(cluster_infor[:, 0].A == cent)[0]]
            # 算出这些数据的中心点
            centroids[cent, :] = np.mean(new_clust, axis=0)
    return centroids, cluster_infor


# 使用外部指标度量聚类性能
def outer_judge(result, models):
    # 获取|SS|
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    n = len(models)
    for i in range(n):
        for j in range(i+1, n):
            if result[i].tolist()[0][0] \
                    == result[j].tolist()[0][0] and models[i] == models[j]:
                count_a += 1
            elif result[i].tolist()[0][0]\
                    == result[j].tolist()[0][0] and models[i] != models[j]:
                count_b += 1
            elif result[i].tolist()[0][0] \
                    != result[j].tolist()[0][0] and models[i] == models[j]:
                count_c += 1
            else:
                count_d += 1
    JC = count_a / (count_a + count_b + count_c)
    FMI = np.sqrt((count_a / (count_a +
                              count_b)) * (count_a / (count_a + count_c)))
    Rand = 2 * (count_a + count_d) / (n * (n-1))
    print('JC系数为：', JC)
    print('FM指数为：', FMI)
    print('Rand指数为：', Rand)


def inner_judge(result, data_set, centroids):
    n = np.shape(result)[0]

    # 用于统计每个类簇中样本所对应在原始数据里的下标
    dic_cluster = {}
    for i in range(n):
        list1 = []
        item = result[i].tolist()[0][0]
        if item not in dic_cluster.keys():
            dic_cluster[item] = list1
        else:
            list1 = dic_cluster[item]
        list1.append(i)
    dic_avg = {}
    for i in dic_cluster:
        total_diatant = 0
        tmp = dic_cluster[i]
        for j in range(len(tmp)):
            for k in range(j + 1, len(tmp)):
                total_diatant += \
                    distant_calc(np.mat(data_set[tmp[j]]), np.mat(data_set[tmp[k]]))
        dic_avg[i] = (total_diatant * 2 / (n * (n - 1)))

    # 计算各个中心点距离
    num_cluster = len(dic_avg)
    total_max = 0
    for i in range(num_cluster):
        max_distant = 0
        for j in range(num_cluster):

            new_distant = (dic_avg[i] + dic_avg[j]) \
                          / distant_calc(np.mat(centroids[i]), np.mat(centroids[j]))
            if new_distant > max_distant:
                max_distant = new_distant
        total_max += max_distant
    DBI = total_max / num_cluster
    print('DB指数为：', DBI)
    return DBI


if __name__ == '__main__':
    k = 6
    # data_set = create_test_data()
    data_set, lables = create_test_data()
    dic = set(lables)
    centroids, result = k_means(np.mat(data_set), k)
    outer_judge(result, lables)
    # min_DBI = 1
    # for i in range(3, 15):
    #     centroids, result = k_means(np.mat(data_set), i)
    #     DBI = inner_judge(result, data_set, centroids)
    #     if DBI < min_DBI:
    #         min_DBI = DBI
    #         k = i

    print('K值为:', k)
    # print('簇坐标', centroids)
    print("特征数：", len(dic))
    print('数据总数', len(data_set), '已分类数据：', np.shape(result)[0])
    dic = {}
    for i in result:
        item = i.tolist()[0][0]
        if item not in dic.keys():
            dic[item] = 0
        dic[item] += 1
    print('分类结果', dic)



