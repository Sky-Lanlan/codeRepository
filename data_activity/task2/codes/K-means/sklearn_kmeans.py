# coding=utf-8
from sklearn.cluster import KMeans


def create_test_data():
    lines_set = open('E:\myCodes\python\mlTest\\venv\src\data\seeds_dataset.txt').readlines()
    data_x = []
    for data in lines_set:
        temp = [i for i in data.split("\n")[0].split("\t") if i is not '']
        data_x.append(list(map(float, temp)))
    return data_x


clf = KMeans(n_clusters=3)
s = clf.fit(create_test_data())
print(clf.cluster_centers_)
# print(clf.labels_)
dic = {}
for i in clf.labels_:
    if i not in dic.keys():
        dic[i] = 0
    dic[i] += 1

print(dic)
