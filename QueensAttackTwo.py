#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):

    # add all squares above, below, and to the sides
    count = 0
    count += (n - 1) * 2

    # add all diagonals
    count += min(n - r_q, n - c_q)
    count += min(r_q - 1, c_q - 1)
    count += min(n - r_q, c_q - 1)
    count += min(r_q - 1, n - c_q)
        
    for obstacle in obstacles:
        r_o = obstacle[0]
        c_o = obstacle[1]

        # Check if the obstacle is in the same row, column, or diagonal as the queen
        if r_o == r_q:
            count -= abs(c_o - c_q) - 1  # Subtract the number of squares blocked in the same row
        elif c_o == c_q:
            count -= abs(r_o - r_q) - 1  # Subtract the number of squares blocked in the same column
        elif abs(r_o - r_q) == abs(c_o - c_q):
            count -= abs(r_o - r_q) - 1  # Subtract the number of squares blocked in the same diagonal




    return count
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()