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


def is_in_maze(cell, num_rows, num_cols):
    return 0 <= cell[0] < num_rows and 0 <= cell[1] < num_cols
