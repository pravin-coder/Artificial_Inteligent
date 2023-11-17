import heapq

def astar(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    open_list = []
    closed_set = set()

    heapq.heappush(open_list, (0, start, []))

    while open_list:
        current_cost, current_pos, path = heapq.heappop(open_list)

        if current_pos == end:
            return path + [current_pos]

        if current_pos in closed_set:
            continue

        closed_set.add(current_pos)

        for move in movements:
            new_pos = (current_pos[0] + move[0], current_pos[1] + move[1])

            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and grid[new_pos[0]][new_pos[1]] == 0:
                new_cost = current_cost + 1
                priority = new_cost + heuristic(new_pos, end)
                heapq.heappush(open_list, (priority, new_pos, path + [current_pos]))

    return None

def heuristic(pos, goal):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

# Example usage:
maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start_point = (0, 0)
end_point = (4, 4)

path = astar(maze, start_point, end_point)

if path:
    print("Path found:", path)
else:
    print("No path found.")
