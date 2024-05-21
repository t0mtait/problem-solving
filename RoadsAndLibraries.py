#!/bin/python3

import math
import os
import random
import re
import sys


def roadsAndLibraries(n, c_lib, c_road, cities):

    # if roads are more expensive or the same price as a library just build a library everywhere:
    if c_lib <= c_road:
        return n * c_lib 
    else:
        # create a connection dictionary
        dict = {i: [] for i in range(1, n+1)}
        for u, v in cities:
            dict[u].append(v)
            dict[v].append(u)

        # create an isVisited bool array for dfs algorithm
        isVisited = [False] * (n+1)


        # begin a depth-first-search through the cities
        def dfs(node):
            isVisited[node] = True
            size = 1
            for neighbor in dict[node]:
                if not isVisited[neighbor]:
                    size += dfs(neighbor)
            return size

        cost = 0
        for i in range(1, n+1):
            if not isVisited[i]:
                size = dfs(i)
                cost += c_lib + (size - 1) * c_road

        return cost




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
