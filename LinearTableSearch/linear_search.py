# -*- coding: utf-8 -*-

""" 实现线性搜索 """

# 算法核心思想：从表的一端开始，顺序扫描数组，依次将扫描到的数组元素和目标值相比较，若当前数组元素与目标值相等，则查找成功；
#             若扫描结束后，仍未找到数组元素等于目标值的结点，则查找失败
# 算法介绍网站：https://zh.wikipedia.org/wiki/%E7%BA%BF%E6%80%A7%E6%90%9C%E7%B4%A2


def linear_search(lists, target):
    """ 实现线性搜索

    Args:
        lists: list
            待搜索的数组

        target: int
            指定搜索元素

    Returns:
        result: int, default = -1
            指定的搜索元素在数组中的位置，如果不存在，则返回-1
    """

    result = -1

    for i, j in enumerate(lists):
        if j == target:
            result = i
            break

    return result


if __name__ == '__main__':
    print u'线性搜索示例：\n'

    array = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
    print u'待搜索的数组：'
    print array

    target = 7
    print u'\n指定搜索元素： ' + str(target)

    result = linear_search(array, target)
    print u'\n搜索结果： ' + str(result)
