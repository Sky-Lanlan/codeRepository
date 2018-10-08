from sklearn import neighbors


def deal_with_res():
    with open('E:\myCodes\python\mlTest\\venv\src\data\iris.data.txt') as file_object:
        contents = file_object.read()
        temp = contents.split("\n")
        slice1 = slice(4)
        slice2 = slice(4, 5)
        data_x = [list2.split(",")[slice1] for list2 in temp]
        data_y = [list2.split(",")[slice2] for list2 in temp]
    i = int(len(data_x) * 2 / 3)
    slice3 = slice(i)
    slice4 = slice(i, len(data_x))
    train_x = data_x[slice3]
    train_y = data_y[slice3]
    test_x = data_x[slice4][:-2]
    test_y = data_y[slice4][:-2]
    return train_x, train_y, test_x, test_y


if __name__ == '__main__':
    kn_clf = neighbors.KNeighborsClassifier(n_neighbors=3)
    X, y, t_x, t_y = deal_with_res()
    kn_clf.fit(X, y)
    kn_y = kn_clf.predict(t_x)
    print(kn_y, t_y)
