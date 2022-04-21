import sys
sys.stdin = open("input.txt", "r")

dic = {}
N, M = map(int, input().split())
for _ in range(N):
    str1, str2 = input().split()
    dic[str1] = str2

for _ in range(M):
    str_temp = input()
    print(dic[str_temp])
