import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def bfs():
    while(dq):
        vals = dq.popleft()
        for i in range(1, 7):
            val_f = vals[0] + i
            if val_f == 100:
                print(vals[1]+1)
                return
            if visit[val_f] == 1 : continue
            visit[val_f] = 1
            if dic.get(val_f, 0) == 0:
                dq.append((val_f, vals[1]+1))
            else:
                dq.append((dic[val_f], vals[1]+1))


N, M = map(int, input().split())

dq = deque([(1, 0)])
dic = dict()
visit = [0]*101
for _ in range(N+M):
    key, val = map(int, input().split())
    dic[key] = val
bfs()