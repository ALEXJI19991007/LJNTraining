class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def construct_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)
    node_8 = TreeNode(8)
    node_9 = TreeNode(9)
    node_10 = TreeNode(10)
    node_11 = TreeNode(11)
    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5
    node_3.left = node_6
    node_3.right = node_7
    node_6.left = node_8
    node_6.right = node_10
    node_8.left = node_9
    node_7.right = node_11
    return node_1


def in_order(root: TreeNode):
    if root is None:
        return
    in_order(root.left)
    print(root.val)
    in_order(root.right)


def pre_order(root: TreeNode):
    if root is None:
        return
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)


def post_order(root: TreeNode):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val)


def lowest_common_ancestor_1(root: TreeNode, one, two):
    if root is None:
        return None
    # if root.val == one or root.val == two:
    #     return root
    left_search_result = lowest_common_ancestor_1(root.left, one, two)
    right_search_result = lowest_common_ancestor_1(root.right, one, two)
    if left_search_result is not None and right_search_result is not None:
        return root
    if root.val == one or root.val == two:
        return root
    if left_search_result is not None:
        return left_search_result
    else:
        return right_search_result
    # A better way:
    # return left_search_result if left_search_result is not None else right_search_result


my_tree_root = construct_tree()
in_order(my_tree_root)
