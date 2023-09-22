def hash_table_intro():
    dictionary = {"red": "apple", "yellow": "pear", "pink": "pig"}
    for x in dictionary.items():
        print(x)
        # key
        print(x[0])
        # value
        print(x[1])


def slb_karat_tree(array_of_tuples):
    nodes_with_one_parent = []
    nodes_without_parent = []
    node_set = set()
    child_parent = {}
    for t in array_of_tuples:
        child = t[1]
        parent = t[0]
        node_set.add(child)
        node_set.add(parent)
        if child not in child_parent:
            child_parent[child] = []
        child_parent[child].append(parent)
    for c in child_parent.items():
        node_set.remove(c[0])
        if len(c[1]) == 1:
            nodes_with_one_parent.append(c[0])
    nodes_without_parent.append(node_set)
    return [nodes_with_one_parent, nodes_without_parent]


def common_numbers_of_two_arrays(array_A, array_B):
    a_occurrence = {}
    result = []
    for a in array_A:
        if a not in a_occurrence:
            a_occurrence[a] = 0
        a_occurrence[a] += 1
    for b in array_B:
        if b in a_occurrence.keys() and a_occurrence[b] > 0:
            result.append(b)
            a_occurrence[b] -= 1
    return result


tuple_array = [(5, 6), (1, 3), (2, 3), (3, 6), (15, 12), (5, 7), (4, 5), (4, 9), (9, 12), (30, 16)]
print(slb_karat_tree(tuple_array))

zhu_A = [1, 2, 3, 3, 3, 4, 5]
zhu_B = [3, 2, 2, 4, 5, 6]
print(common_numbers_of_two_arrays(zhu_A, zhu_B))
