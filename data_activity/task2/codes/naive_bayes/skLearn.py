from sklearn.naive_bayes import GaussianNB
import random


# 读取数据文档中的训练数据（生成二维列表）
def load_train_data(k):
    lines_set = open('PhishingData.arff.txt').readlines()
    data = []
    for temp in lines_set:
        temp2 = list(temp[:].split("\n")[0].split(","))
        tmp = []
        for i in temp2:
            tmp.append(float(i))
        data.append(tmp[:])
    list1 = list(range(0, len(data), k))
    w = random.sample(list1, 1)[0]
    data_x = []
    data_x.extend(data[:w])
    data_x.extend(data[w + int(len(data) / k):])
    data_y = [i[-1:][0] for i in data_x]
    data_x = [i[:-1] for i in data_x]
    test_y = [i[-1:][0] for i in data[w:w +
                                     int(len(data) / k)]]
    test_x = [i[:-1] for i in data[w:w + int(len(data) / k)]]
    return data_x, data_y, test_x, test_y


if __name__ == '__main__':
    k = 10
    avg_accuracy = 0
    for i in range(k):
        count = 0
        x, y, t_x, t_y= load_train_data(k)
        clf = GaussianNB()
        clf.fit(x, y)
        predict = clf.predict(t_x)

        total = len((t_x))
        for j in range(len(t_y)):
            if predict[j] == t_y[j]:
                count += 1
        accuracy = count / total * 100
        print("第", (i + 1), "次测试准确率为：", accuracy, "%")
        avg_accuracy += accuracy / k
        if i == k - 1:
            print("样本数量为：", len(x))
            print("测试数量为：", len(t_x))
            print("属性类为：", len(x[0]))
            print("测试平均准确率为：", avg_accuracy, "%")

