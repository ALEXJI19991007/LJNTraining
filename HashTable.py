def hash_table_intro():
    dictionary = {"red": "apple", "yellow": "pear", "pink": "pig"}
    for x in dictionary.items():
        print(x)
        # key
        print(x[0])
        # value
        print(x[1])


# Time Complexity: O(N) where N is the length of array_of_tuples
# Space Complexity: O(N)
def slb_karat_tree(array_of_tuples):
    # These are the answers
    nodes_with_one_parent = []
    nodes_without_parent = []
    # This set is to record all nodes
    node_set = set()
    # This dictionary is used to record the relationship between a child and its parents (may have more than 2 parents)
    # E.g.: 1: [5, 6] --> this means 1 has two parents, which are 5 and 6
    child_parent = {}
    for t in array_of_tuples:
        child = t[1]
        parent = t[0]
        node_set.add(child)
        node_set.add(parent)
        if child not in child_parent:
            child_parent[child] = []
        child_parent[child].append(parent)
    # Currently the node_set records all nodes. We need to iterate through the child_parent dictionary to remove
    # those nodes who have parents from the node_set.
    for c in child_parent.items():
        node_set.remove(c[0])
        if len(c[1]) == 1:
            nodes_with_one_parent.append(c[0])
    # Currently, the node_set only contains nodes without parents
    nodes_without_parent.append(node_set)
    return [nodes_with_one_parent, nodes_without_parent]


# Time Complexity: O(N)
# Space Complexity: O(N)
def slb_karat_tree_2(array_of_tuples, node_1, node_2):
    child_parent = {}
    for t in array_of_tuples:
        child = t[1]
        parent = t[0]
        if child not in child_parent:
            child_parent[child] = []
        child_parent[child].append(parent)
    # Level order traversal for node_1 -- put all ancestors of node_1 into the queue layer by layer (from bottom to up)
    ancestor_node_1 = level_order_traversal(child_parent, node_1)
    ancestor_node_1_set = set(ancestor_node_1)
    # Level order traversal for node_2
    ancestor_node_2 = level_order_traversal(child_parent, node_2)
    for node in ancestor_node_2:
        if node in ancestor_node_1_set:
            return node
    return None


def level_order_traversal(child_parent, node):
    ancestors = []  # This is where we store the solution
    queue = [node]
    while len(queue) > 0:
        size = len(queue)
        for i in range(size):
            cur_node = queue.pop(0)
            ancestors.append(cur_node)
            cur_node_parents = child_parent[cur_node]
            for parent in cur_node_parents:
                queue.append(parent)
    return ancestors


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
