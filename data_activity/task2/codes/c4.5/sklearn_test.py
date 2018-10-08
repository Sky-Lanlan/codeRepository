from sklearn import tree
from sklearn.externals.six import StringIO
import pydot
from sklearn.datasets import load_iris

# 读取数据文档中的训练数据（生成二维列表）
def create_train_data():
    lines_set = open('E:\myCodes\python\mlTest\\venv\src\data\\winequality-red.csv').readlines()
    data_x = []
    labels = []
    for temp in lines_set:
        # 将标签移至最后一列
        temp2 = list(temp[:].split("\n")[0].split(";"))
        print(temp2)
        labels.append(list(map(float,temp2[-1:])))
        data_x.append(list(map(float,temp2[:-1])))

    return data_x, labels

# 读取数据文档中的测试数据（生成二维列表）
def create_test_data():
    lines_set = open('E:\myCodes\python\mlTest\\venv\src\data\winequality-red_test.txt').readlines()
    data_x = []
    data_y = []
    for temp in lines_set:
        temp2 = list(temp[:].split("\n")[0].split(";"))
        print(temp2)
        data_y.append(list(map(float, temp2[-1:])))
        data_x.append(list(map(float, temp2[:-1])))
    return data_x, data_y


if __name__ == '__main__':
    my_dat_x, labels = create_train_data()
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(my_dat_x, labels)
    test_list, test_labels = create_test_data()
    w = clf.predict(test_list)
    # print(len(my_dat_x))
    # dot_data = StringIO()
    # tree.export_graphviz(clf, out_file=dot_data)
    # graph = pydot.graph_from_dot_data(dot_data.getvalue())
    # graph[0].write_dot('iris_simple.dot')
    # graph[0].write_png('iris_simple.png')
    total = len(w)
    counter = 0
    for i in range(total):
        print(w[i], test_labels[i])
        if w[i] == test_labels[i]:
            counter += 1
    print(counter/total*100, "%")

