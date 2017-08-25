# -*- coding: utf-8 -*-

""" 实现二分查找 """

# 算法核心思想：搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜索过程结束；如果某一特定元素大于或者小于中间元素，
#             则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。如果在某一步骤数组为空，则代表找不到
# 算法介绍网址：https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2%E7%AE%97%E6%B3%95


def binary_search(lists, start, end, target):
    """ 实现二分查找

    Args:
        lists: list
            待搜索的数组

        start: int
            二分查找起始位置

        end: int
            二分查找终止位置

        target: int
            指定搜索元素

    Returns:
        result: int, default = -1
            指定的搜索元素在数组中的位置，如果不存在，则返回-1
    """

    result = -1

    if start > end:
        return result

    mid = (start + end) / 2

    if lists[mid] == target:
        return mid

    if lists[mid] < target:
        return binary_search(lists, start, mid, target)

    if lists[mid] > target:
        return binary_search(lists, mid, end, target)


if __name__ == '__main__':
    print u'二分搜索示例：\n'

    array = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
    print u'待搜索的数组：'
    print array

    target = 7
    print u'\n指定搜索元素： ' + str(target)

    result = binary_search(array, 0, len(array) - 1, target)
    print u'\n搜索结果： ' + str(result)
