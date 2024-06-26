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
    count = 0

    # up
    r = r_q + 1
    while r <= n:
        if [r, c_q] in obstacles:
            break
        count += 1
        r += 1

    # down
    r = r_q - 1
    while r >= 1:
        if [r, c_q] in obstacles:
            break
        count += 1
        r -= 1

    # left
    c = c_q - 1
    while c >= 1:
        if [r_q, c] in obstacles:
            break
        count += 1
        c -= 1

    # right
    c = c_q + 1
    while c <= n:
        if [r_q, c] in obstacles:
            break
        count += 1
        c += 1

    # up-right
    r, c = r_q + 1, c_q + 1
    while r <= n and c <= n:
        if [r, c] in obstacles:
            break
        count += 1
        r += 1
        c += 1

    # up-left
    r, c = r_q + 1, c_q - 1
    while r <= n and c >= 1:
        if [r, c] in obstacles:
            break
        count += 1
        r += 1
        c -= 1

    # down-right
    r, c = r_q - 1, c_q + 1
    while r >= 1 and c <= n:
        if [r, c] in obstacles:
            break
        count += 1
        r -= 1
        c += 1

    # down-left
    r, c = r_q - 1, c_q - 1
    while r >= 1 and c >= 1:
        if [r, c] in obstacles:
            break
        count += 1
        r -= 1
        c -= 1

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