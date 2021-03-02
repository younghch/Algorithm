"""
[문제]
각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders, 스카피가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course가 매개변수로 주어질 때, 스카피가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

[제한사항]
orders 배열의 크기는 2 이상 20 이하입니다.
orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.
각 문자열은 알파벳 대문자로만 이루어져 있습니다.
각 문자열에는 같은 알파벳이 중복해서 들어있지 않습니다.
course 배열의 크기는 1 이상 10 이하입니다.
course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있습니다.
course 배열에는 같은 값이 중복해서 들어있지 않습니다.
정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return 해주세요.
배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
orders와 course 매개변수는 return 하는 배열의 길이가 1 이상이 되도록 주어집니다.
"""
import collections
import itertools


def solution1(orders, course):
    answer = []
    menus = set()
    order_dic = collections.defaultdict(set)
    for i in range(len(orders)):
        for c in orders[i]:
            menus.add(c)
            order_dic[(c, )].add(i)
    menus = sorted(list(menus))
    for j in range(2, max(course) + 1):
        keys = itertools.combinations(menus, j)
        for key in keys:
            new_set = order_dic[key[:-1]] & order_dic[(key[-1],)]
            if len(new_set) == 0:
                continue
            order_dic[key] = new_set
    ans_dic = collections.defaultdict(list)
    for key in order_dic:
        if len(key) not in course:
            continue
        longs = ans_dic[len(key)]
        if len(longs) == 0:
            if len(order_dic[key]) < 2:
                continue
            longs.append(len(order_dic[key]))
            longs.append(key)
            continue

        if longs[0] == len(order_dic[key]):
            ans_dic[len(key)].append(key)
            continue

        if longs[0] < len(order_dic[key]):
            ans_dic[len(key)] = [len(order_dic[key]), key]
    for value in ans_dic.values():
        for i in range(1, len(value)):
            answer.append(''.join(list(value[i])))
    answer.sort()
    return answer


def solution2(orders, course):
    result = []
    sorted_orders = []
    for order in orders:
        sorted_orders.append(sorted(order))
    for course_size in course:
        order_combination = []
        for order in sorted_orders:
            order_combination += (itertools.combinations(order, course_size))
        most_ordered = collections.Counter(order_combination).most_common()
        result += [key for key, value in most_ordered if value > 1 and value == most_ordered[0][1]]
    return [''.join(v) for v in sorted(result)]
solution2(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])
