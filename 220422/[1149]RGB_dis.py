import sys
from itertools import *

sys.stdin = open("input.txt", "r")

N = int(input())
List = [list(map(int, input().split())) for _ in range(N)]
Min = 21e8
pre_i = -1

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
i, j = 0, 0
pre_j = -1

for cwr in combinations_with_replacement(range(N), 8):
    if cwr[0] == cwr[1] or cwr[N]:
        continue
    flag = 0
    for i in range(1, N):
        if cwr[i-1] == cwr[i]:
            flag = 1
            break
    for i in range(1, N-1):
        if cwr[i] == cwr[i-1] or cwr[i] == cwr[i+1]:
            flag = 1
            break
    if flag == 1:
        continue
    print(cwr)
