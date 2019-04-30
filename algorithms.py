def depth_first(maze, x, y, path):

    if maze[y][x] == 9:
        path.append([x, y])
        return True

    if maze[y][x] == 0:
        maze[y][x] = 2

        dx = -1
        dy = 0
        if depth_first(maze, x + dx, y + dy, path):
            path.append([x, y])
            return True
        
        dx = 1
        dy = 0
        if depth_first(maze, x + dx, y + dy, path):
            path.append([x, y])
            return True
        
        dx = 0
        dy = -1
        if depth_first(maze, x + dx, y + dy, path):
            path.append([x, y])
            return True

        dx = 0
        dy = 1
        if depth_first(maze, x + dx, y + dy, path):
            path.append([x, y])
            return True

    return False