import collections
test = [1, 2, 3, 4]


def rec():
    for i in range(4):
        if test[i] == 4:
            print(i, " is four!!")
            continue
        else:
            test[i] += 1
            print("rec", i)
            rec()

rec()

