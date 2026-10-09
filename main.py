"""
Simple 2D grid game prototype.

A 10x10 grid with a player '@' that can move using WASD.
Press 'q' to quit.
"""

import sys

WIDTH, HEIGHT = 10, 10
EMPTY, PLAYER, BLOCK = '.', '@', '#'

def init_grid():
    grid = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]
    # place some blocks
    for i in range(2, 8):
        grid[5][i] = BLOCK
    return grid

def draw(grid, pos):
    for y, row in enumerate(grid):
        print(''.join(PLAYER if (x, y) == pos else cell for x, cell in enumerate(row)))
    print()

def move(pos, direction, grid):
    x, y = pos
    if direction == 'w': y -= 1
    elif direction == 's': y += 1
    elif direction == 'a': x -= 1
    elif direction == 'd': x += 1
    if 0 <= x < WIDTH and 0 <= y < HEIGHT and grid[y][x] != BLOCK:
        pos = (x, y)
    return pos

def main():
    grid = init_grid()
    pos = (0, 0)
    while True:
        draw(grid, pos)
        cmd = input("Move (WASD) or Q to quit: ").lower()
        if cmd == 'q':
            print("Bye!")
            break
        if cmd in 'wasd':
            pos = move(pos, cmd, grid)

if __name__ == "__main__":
    main()