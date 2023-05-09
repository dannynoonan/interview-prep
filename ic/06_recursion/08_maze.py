# 08
# Medium

# Maze Problem: You are given a 2D array that represents a maze. 
# It can have 2 values - 0 and 1.
# 1 represents a wall and 0 represents a path.
# The objective is to reach the bottom right corner, i.e, A[A.length-1][A.length-1]. 
# You start fromA[0][0]. You can move in 4 directions - up, down, left and right. 
# Find if a path exists to the bottom right of the maze.

# For example, a path exists in the following maze:
# 0 1 1 1
# 0 1 1 1
# 0 0 0 0
# 1 1 1 0


# -----------------------------------------------------

# Time Complexity:​ O(n) with memoization, where ​n​ is the number of elements in the matrix
# Space Complexity:​ O(n) on both the memo and the recursion stack

def build_visited(x: int, y: int) -> list:
    visited = [None] * y
    for i in range(y):
        visited[i] = [False] * x
    return visited

directions = [(-1,0),(0,-1),(1,0),(0,1)]

def navigate_maze_main(maze: list) -> bool:
    visited = build_visited(len(maze[0]), len(maze))
    if navigate_maze(maze, 0, 0, visited):
        print("Escaped!")
        return True
    else:
        print("No way out")
        return False

def navigate_maze(maze: list, x: int, y: int, visited: list) -> bool:
    # print(f"processing [{x},{y}]")
    if x == len(maze[0])-1 and y == len(maze)-1:
        print("Reached exit!")
        return True
    if x < 0 or x == len(maze[0]) or y < 0 or y == len(maze):
        # print(f"OOB at [{x},{y}]")
        return False
    if maze[y][x] == 1:
        # print(f"Hit a wall at [{x},{y}]")
        visited[y][x] = True
        return False
    if visited[y][x]:
        # print(f"Already visited [{x},{y}]")
        return False
    visited[y][x] = True
    print(f"VISITING [{x},{y}]")
    for d in directions:
        new_x = x + d[0]
        new_y = y + d[1]
        if navigate_maze(maze, new_x, new_y, visited):
            return True

# -----------------------------------------------------

maze1 = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [0,1,1,0,0]
]

navigate_maze_main(maze1)

maze2 = [
    [0,1,0,0,0,0,0,0],
    [0,1,0,1,0,1,0,0],
    [0,0,0,1,0,0,0,1],
    [0,1,1,0,0,1,1,0],
    [0,0,1,0,1,0,0,0],
    [1,0,1,0,0,0,1,0]
]

navigate_maze_main(maze1)
navigate_maze_main(maze1)
