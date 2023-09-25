def search_in_maze_bfs(maze, start, end):
    num_rows = len(maze)
    num_cols = len(maze[0])
    queue = []
    visited_cell = set()
    queue.append(start)
    visited_cell.add(start)
    while len(queue) != 0:
        size = len(queue)
        for i in range(size):
            cur_cell = queue.pop(0)
            if cur_cell[0] == end[0] and cur_cell[1] == end[1]:
                return True
            upper_cell = (cur_cell[0] - 1, cur_cell[1])
            right_cell = (cur_cell[0], cur_cell[1] + 1)
            bottom_cell = (cur_cell[0] + 1, cur_cell[1])
            left_cell = (cur_cell[0], cur_cell[1] - 1)
            neighbor = [upper_cell, right_cell, bottom_cell, left_cell]
            for cell in neighbor:
                if is_in_maze(cell, num_rows, num_cols) and cell not in visited_cell:
                    queue.append(cell)
                    # We make sure the cell is not added to the queue twice
                    visited_cell.add(cell)
    return False


class Node:
    def __init__(self, val=0, neighbors: list=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Time Complexity = O(N) where N is the number of nodes
# Space Complexity = O(N)
def count_connected_components(node_list: list[Node]) -> int:
    if node_list is None or len(node_list) == 0:
        return 0
    cc_count = 0
    visited_set = set()
    for node in node_list:
        if node.val in visited_set:
            continue
        queue = [node]
        visited_set.add(node.val)
        while len(queue) != 0:
            size = len(queue)
            for i in range(size):
                cur_node = queue.pop(0)
                neighbors = cur_node.neighbors
                for neighbor in neighbors:
                    if neighbor.val not in visited_set:
                        visited_set.add(neighbor.val)
                        queue.append(neighbor)
        cc_count += 1
    return cc_count


# Time Complexity = O(N) where N is the number of nodes in the cc
# Space Complexity = O(N)
def count_nodes_in_cc(node: Node) -> int:
    if node is None:
        return 0
    queue = []
    visited = set()
    count = 1
    queue.append(node)
    visited.add(node.val)
    while len(queue) != 0:
        size = len(queue)
        for i in range(size):
            cur_node = queue.pop(0)
            neighbors = cur_node.neighbors
            for neighbor in neighbors:
                if neighbor.val not in visited:
                    visited.add(neighbor.val)
                    queue.append(neighbor)
                    count += 1
    return count


def is_in_maze(cell, num_rows, num_cols):
    return 0 <= cell[0] < num_rows and 0 <= cell[1] < num_cols


def generate_graph():
    node_1 = Node(1, [])
    node_2 = Node(2, [])
    node_3 = Node(3, [])
    node_1.neighbors = [node_2, node_3]
    node_2.neighbors = [node_1, node_3]
    node_3.neighbors = [node_1, node_2]

    node_4 = Node(4, [])
    node_5 = Node(5, [])
    node_6 = Node(6, [])
    node_4.neighbors = [node_5, node_6]
    node_5.neighbors = [node_4, node_6]
    node_6.neighbors = [node_4, node_5]

    return [node_1, node_2, node_3, node_4, node_5, node_6]


array_of_nodes = generate_graph()
print(count_connected_components(array_of_nodes))

node_1 = Node(1, [])
node_2 = Node(2, [])
node_3 = Node(3, [])
node_1.neighbors = [node_2, node_3]
node_2.neighbors = [node_1, node_3]
node_3.neighbors = [node_1, node_2]
print(count_nodes_in_cc(node_1))
