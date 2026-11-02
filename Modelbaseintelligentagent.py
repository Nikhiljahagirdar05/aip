# Implement the modelbased intelligent agent capable of navigating a grid environment with obstacles using internal state representation

grid=[
    ["S", ".", "#"],
    [".", "#", "."],
    [".", ".", "G"]
]

position=(0,0)
visited=set()

while True:
    x,y=position
    visited.add(position)
    print("Current Position", position)

    if grid[x][y] == 'G':
        print("Goal Reached...")
        break

    moves=[(1,0),(0,1),(-1,0),(0,-1)]

    for dx,dy in moves:
        nx,ny= x+dx, y+dy

        if 0 <= nx < 3 and 0 <= ny < 3 and grid[nx][ny]!='#' and (nx,ny) not in visited:
            position=(nx,ny)
            break
    else:
        print("No path found")
        break