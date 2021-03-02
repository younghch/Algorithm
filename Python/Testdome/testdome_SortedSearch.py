""""
Implement function count_numbers that accepts a sorted list of unique integers and, efficiently with respect to time used, counts the number of list elements that are less than the parameter less_than.

For example, count_numbers([1, 3, 5, 7], 4) should return 2 because there are two list elements less than 4.
"""


def count_numbers(sorted_list, less_than):
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] < less_than:
            left = mid + 1
        else:
            right = mid - 1
    return left


if __name__ == "__main__":
    sorted_list = [1, 2, 3, 5, 7]
    print(count_numbers(sorted_list, 8)) # should print 2
