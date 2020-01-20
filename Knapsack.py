import math
from copy import deepcopy

def create_2D_Matrix(R, C, v):
    return [[(v, -1) for c in range(C)] for r in range(R)]

def glory_Print(cw, cv, cur):
    print("Current Item : ({}, {})".format(cw, cv))
    for row in cur:
        for val in row:
            print(val, end=' ')
        print("")

def solve_knapsack(weights, max_weight=20, max_items=4):
    mat = []
    cur = create_2D_Matrix(max_items+1, max_weight+1, -1000000000)
    cur[0][0] = (0, -1)

    mat.append(cur)
    # glory_Print(0, 0, cur)
    for i, (cw, cv) in enumerate(weights):
        prev = mat[-1]
        cur = deepcopy(prev)
        for n in range(1, max_items+1):
            for w in range (cw, max_weight+1):
                if cv + prev[n-1][w-cw][0] > cur[n][w][0]:
                    cur[n][w] = (cv + prev[n-1][w-cw][0], i)
        mat.append(cur)
        # glory_Print(cw, cv, cur)
    
    mm = 0
    r = 0
    c = 0
    for n in range(0, max_items+1):
        for w in range(0, max_weight+1):
            if cur[n][w][0] > mm:
                r = n
                c = w
                mm = cur[n][w][0]

    res = []
    cur_idx = len(weights)
    for cur in reversed(mat):
        cur_idx -= 1
        if (cur_idx < 0):
            break
        idx = cur[r][c][1]
        if idx == cur_idx:
            res.append(idx)
            r = r -1
            c = c - weights[idx][0]

    return res[::-1]

if __name__ == "__main__":
    # weights_values=[(1, 4), (5, 3), (5, 2), (3, 7), (2, 3)]     # list of (weight, value) pairs
    weights_values = []
    import random
    for i in range(50):
        x = random.randint(8, 100)
        y = random.randint(85, 100)
        weights_values.append((x, y))
    result = solve_knapsack(weights_values, 100, 6)

    for r in result:
        print(weights_values[r])

    print(result)
    print("-----------")
    print(weights_values)

