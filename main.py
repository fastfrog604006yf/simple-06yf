We need to write a small, complete, runnable Python project about a simple 2D grid game prototype. Requirements:

- single file
- under 60 lines
- short module docstring
- standard library only
- include a __main__ block

We need to output code only.

It has to be a simple 2D grid game prototype. It could be like a console-based grid where the player moves around, maybe avoid obstacles. Probably use curses? But curses might not be available on Windows. Use simple print. Use random for placing obstacles. Use input() for movement. The grid could be a list of strings. Represent player with '@', obstacles with '#', empty with '.'. The player can move with WASD. The game ends when the player reaches the goal 'G' or quits with 'q'.

Under 60 lines. So we need to count lines. Let's plan:

1: docstring
2: imports
3: maybe: import random, sys

Then define main:

def main():
    grid size 10x10
    place player at (0,0)
    place goal at (9,9)
    place obstacles randomly (maybe 15)
    loop:
        print grid
        read input
        update pos
        check for win/lose
        if quit: break

This can be done under 60 lines.

We need to handle input: maybe use input() to ask for direction. Use 'w','a','s','d' for movement, 'q' to quit.

Simplify: We can represent grid as 2D list of chars.

Print grid: For each row, print(''.join(row)). Or maybe add row numbers.

Let's count lines. We'll aim ~45 lines.

Docstring: 1-2 lines.

Imports: 1 line.

Main function: line ~2.

Set grid size: 8 lines.

Place obstacles: loop.

Game loop: while True.

In loop: print grid, input direction.

Move logic: check boundaries and obstacles.

Check win.

Break on quit.

If __name__ == "__main__": main()

Need to keep under 60 lines. Let's write code and count.

We'll write:

"""Simple 2D grid game prototype"""

import random

def main():
    width, height = 10, 10
    player = [0, 0]
    goal = [height-1, width-1]
    grid = [['.' for _ in range(width)] for _ in range(height)]
    # place obstacles
    for _ in range(20):
        r, c = random.randrange(height), random.randrange(width)
        if (r, c) not in [(player[0], player[1]), tuple(goal)]:
            grid[r][c] = '#'
    def draw():
        for r in range(height):
            row = ''
            for c in range(width):
                if [r, c] == player:
                    row += '@'
                elif [r, c] == goal:
                    row += 'G'
                else:
                    row += grid[r][c]
            print(row)
        print("Move with WASD, q to quit.")
    while True:
        draw()
        move = input().lower()
        if move == 'q':
            print("Quit.")
            break
        dr, dc = 0, 0
        if move == 'w':
            dr = -1
        elif move == 's':
            dr = 1
        elif move == 'a':
            dc = -1
        elif move == 'd':
            dc = 1
        new_r, new_c = player[0] + dr, player[1] + dc
        if 0 <= new_r < height and 0 <= new_c < width and grid[new_r][new_c] != '#':
            player[0], player[1] = new_r, new_c
        if player == goal:
            draw()
            print("You win!")
            break

if __name__ == "__main__":
    main()

Count lines: Let's count. We'll count each line including blank lines.

1: """Simple 2D grid game prototype"""
2: 
3: import random
4:
5: def main():
6:     width, height = 10, 10
7:     player = [0, 0]
8:     goal = [height-1, width-1]
9:     grid = [['.' for _ in range(width)] for _ in range(height)]
10:     # place obstacles
11:     for _ in range(20):
12:         r, c = random.randrange(height), random.randrange(width)
13:         if (r, c) not in [(player[0], player[1]), tuple(goal)]:
14:             grid[r][c] = '#'
15:     def draw():
16:         for r in range(height):
17:             row = ''
18:             for c in range(width):
19:                 if [r, c] == player:
20:                     row += '@'
21:                 elif [r, c] == goal:
22:                     row += 'G'
23:                 else:
24:                     row += grid[r][c]
25:             print(row)
26:         print("Move with WASD, q to quit.")
27:     while True:
28:         draw()
29:         move = input().lower()
30:         if move == 'q':
31:             print("Quit.")
32:             break
33:         dr, dc = 0, 0
34:         if move == 'w':
35:             dr = -1
36:         elif move == 's':
37:             dr = 1
38:         elif move == 'a':
39:             dc = -1
40:         elif move == 'd':
41:             dc = 1
42:         new_r, new_c = player[0] + dr, player[1] + dc
43:         if 0 <= new_r < height and 0 <= new_c < width and grid[new_r][new_c] != '#':
44:             player[0], player[1] = new_r, new_c
45:         if player == goal:
46:             draw()
47:             print("You win!")
48:             break
49:
50: if __name__ == "__main__":
51:     main()

Line 50 and 51. That's 51 lines. Under 60 lines. Good.

But we used tuple(goal). Let's ensure goal is list [height-1,width-1], so tuple(goal) works. However we used (player[0], player[1]) tuple. For clarity, maybe convert both to tuples. That is fine.

One improvement: In obstacle placement, we might have duplicates: the loop random 20 obstacles but might place same cell again? The condition ensures not placing on player or goal but duplicates possible among obstacles. Not a big issue.

We use input() which blocks. It's fine.

We might want to flush screen. But not necessary.

The code is under 60 lines. Provide code only.

Add a short module docstring