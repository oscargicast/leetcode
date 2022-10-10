"""
Example 3: Given two sorted integer arrays, return an array that combines both of them and is also sorted.
"""


def mix_sorted_lists(list1, list2):
    sorted_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1
    while j < len(list2):
        sorted_list.append(list2[j])
        j += 1
    while i < len(list1):
        sorted_list.append(list1[i])
        i += 1
    return sorted_list


if __name__ == "__main__":
    assert(mix_sorted_lists(
        [1, 2, 5, 14],
        [3, 6, 7],
    ) == [1, 2, 3, 5, 6, 7, 14]) 
    assert(mix_sorted_lists(
        [1, 2, 3],
        [3, 6, 7],
    ) == [1, 2, 3, 3, 6, 7]) 
