import numpy as np
import matplotlib.pyplot as plt
from itertools import groupby


def print_result(array):
    ax = plt.axes()
    ax.set_xticks(np.arange(0.5, len(constraint_y) + 0.5, 1))
    ax.set_xticklabels(constraint_y, rotation='vertical')
    ax.xaxis.set_ticks_position('top')
    ax.set_yticks(np.arange(len(constraint_x) - 0.5, 0, -1))
    ax.set_yticklabels(constraint_x)
    ax.xaxis.set_minor_locator(plt.FixedLocator(np.arange(0,len(constraint_y), 1)))
    ax.yaxis.set_minor_locator(plt.FixedLocator(np.arange(0,len(constraint_y), 1)))
    ax.grid(which='minor', axis='x', linewidth=1.25, linestyle='-', color='0.25')
    ax.grid(which='minor', axis='y', linewidth=1.25, linestyle='-', color='0.25')
    img = plt.imshow(array, cmap='gray_r', vmin=0, vmax=1, interpolation='none', origin="upper", rasterized=True,  extent=[0, array.shape[1], 0, array.shape[0]])
    plt.tight_layout()
    plt.show()

def findSolution(i, j):
    if i == board.shape[0]:
        return True
    if j + 1 == board.shape[1]:
        nextI = i + 1
    else:
        nextI = i
    nextJ = (j + 1) % board.shape[1]

    board[i][j] = 1
    if verify(i, j) and findSolution(nextI, nextJ):
        return True

    board[i][j] = 0
    if verify(i, j) and findSolution(nextI, nextJ):
        return True
    return False


def verify(i, j):
    if group_size(i, j):
        return True
    else:
        return False


def group_size(i, j):

    summ = [sum(b) for _, b in groupby(board[i, :])]
    # check if last column, and sum of row is equal to sum of requirements
    if j == nonogram_size[0]-1 and sum(summ) < sum(requirements_x[i]):
        return False
    board_current = [g for g in summ if g != 0]

    # check if number of groups is bigger than requirements
    if len(board_current) > len(requirements_x[i]):
        return False

    # check if each group size is more than requirements
    for counter, k in enumerate(board_current):
        if k > requirements_x[i][counter]:
            return False

    summ = [sum(b) for _, b in groupby(board[:, j])]

    if i == nonogram_size[1]-1 and sum(summ) < sum(requirements_y[j]):

        return False
    board_current = [g for g in summ if g != 0]
    if len(board_current) > len(requirements_y[j]):

        return False
    for counter, k in enumerate(board_current):
        if k > requirements_y[j][counter]:

            return False
    return True


if __name__ == '__main__':
    # nonogram_size = [5, 5]
    # requirements_x = [[3, 1],
    #                   [2],
    #                   [2],
    #                   [4],
    #                   [5]]
    #
    # requirements_y = [[1, 1, 1],
    #                   [1, 3],
    #                   [1, 2],
    #                   [1, 2],
    #                   [2, 2]]

    nonogram_size = [10, 10]
    requirements_x = [[2, 1, 4],
                      [5, 2, 1],
                      [2, 1, 2],
                      [1, 7],
                      [2, 1],
                      [1, 3, 3],
                      [2, 3],
                      [4],
                      [2, 1, 1, 2],
                      [1]]

    requirements_y = [[7, 1],
                      [3, 1, 3],
                      [1, 1, 1, 1],
                      [9],
                      [1, 1, 3],
                      [1, 1],
                      [2, 1, 1, 1],
                      [2, 1, 1],
                      [1, 2, 1, 1],
                      [3, 2]]

    # nonogram_size = [7, 7]
    # requirements_x = [[1, 4],
    #                   [3, 1],
    #                   [2, 2],
    #                   [5, 1],
    #                   [1, 3],
    #                   [1, 2],
    #                   [3, 1]]
    #
    # requirements_y = [[1, 2],
    #                   [2, 1],
    #                   [4, 1],
    #                   [2, 1, 2],
    #                   [5],
    #                   [1, 1, 2],
    #                   [1, 4]]


    # nonogram_size = [7, 7]
    # requirements_x = [[4, 2],
    #                   [1, 1, 1],
    #                   [3],
    #                   [1, 1, 1],
    #                   [2, 2],
    #                   [4, 2],
    #                   [5, 1]]
    #
    # requirements_y = [[1, 2],
    #                   [2, 3],
    #                   [1, 4],
    #                   [3, 2],
    #                   [3, 1],
    #                   [3, 2],
    #                   [1, 1, 2]]


    # nonogram_size = [10, 10]
    # requirements_x = [[2, 1],
    #                   [1, 2],
    #                   [6],
    #                   [3, 4],
    #                   [1, 2],
    #                   [1, 3, 1],
    #                   [6, 2],
    #                   [8],
    #                   [2, 6],
    #                   [6]]
    #
    # requirements_y = [[1, 5],
    #                   [1, 4],
    #                   [1, 2, 1],
    #                   [1, 2, 4],
    #                   [2, 4],
    #                   [2, 5],
    #                   [2, 1, 2],
    #                   [2, 4],
    #                   [4, 1, 1],
    #                   [5]]

    global board
    global constraint_x
    global constraint_y
    board = np.zeros(nonogram_size, dtype="int")
    constraint_x = requirements_x
    constraint_y = requirements_y
    findSolution(0, 0)
    print_result(board)

