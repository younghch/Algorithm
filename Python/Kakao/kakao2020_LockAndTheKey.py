


import collections


def rotate_lock(key):
    rotated = [[] for _ in range(len(key[0]))]
    reversed_key = list(reversed(key))
    for row in reversed_key:
        for c, col in enumerate(row):
            rotated[c].append(col)
    return rotated


def compare(key, lock):



def solution(key, lock):
    lock = len()
    return answer


print(rotate_key(rotate_key([[1], [4], [7]])))

