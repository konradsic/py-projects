# https://www.youtube.com/watch?v=G_UYXzGuqvM <- tutorial
import random
import sys

sys.setrecursionlimit(10 ** 9)

matrix = []
for x in range(9):
    nums = list(map(int, list(
        input().strip("\n ").split(" ")
    )))
    matrix.append(nums)


def show_sudoku_grid():
    global matrix
    # output a sudoku grid as 3x3 chunks
    for line in matrix:
        for i, num in enumerate(line, start=1):
            if i % 3 == 0:
                print(num, end="   ")
            else:
                print(num, end="")
        print()


def possible(y, x, n):
    global matrix
    for i in range(0, 9):
        if matrix[y][i] == n:
            return False
        elif matrix[i][x] == n:
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if matrix[y0 + i][x0 + j] == n:
                return False
    return True


def solve():
    global matrix
    for y in range(9):
        for x in range(9):
            if matrix[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        matrix[y][x] = n
                        solve()
                        matrix[y][x] = 0

                return
    show_sudoku_grid()
    print("="*25)
    input("More? ")

show_sudoku_grid()
print("="*25)
solve()
# show_sudoku_grid(matrix)

