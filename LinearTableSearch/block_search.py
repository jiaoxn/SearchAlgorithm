# -*- coding: utf-8 -*-

""" 实现分块查找 """


def build_block_index_array(lists, n_block):
    """ 构建块的索引列表

    Args:
        lists: list
            待排序数组

        n_block: int
            块的个数

    Returns:
        index_array: lists
            待排序数组的块索引列表
    """

    block_size = len(lists) / n_block if len(lists) % n_block == 0 else len(lists) / n_block + 1  # 块的大小

    index_array = [[] for _ in range(n_block)]

    for i in range(n_block):
        block_start = i * block_size
        block_end = (i + 1) * block_size if (i + 1) * block_size <= len(lists) else len(lists)

        block_min, block_max = lists[block_start], lists[block_start]

        for j in lists[block_start:block_end]:
            if j < block_min:
                block_min = j

            if j > block_max:
                block_max = j

        index_array[i].append(block_start)
        index_array[i].append(block_end)
        index_array[i].append(block_min)
        index_array[i].append(block_max)

    return index_array


def block_search(lists, target):
    """ 块搜索

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

    block_index_arrays = build_block_index_array(lists, 3)

    for block_index_array in block_index_arrays:
        if target in range(block_index_array[2], block_index_array[3] + 1):
            # 执行顺序查找/二分查找

            for i in range(block_index_array[0], block_index_array[1]):
                if target == lists[i]:
                    result = i

                    return result

    return result


if __name__ == '__main__':
    print u'块搜索示例：\n'

    array = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
    print u'待搜索的数组：'
    print array

    target = 7
    print u'\n指定搜索元素： ' + str(target)

    result = block_search(array, target)
    print u'\n搜索结果： ' + str(result)
