import sys
sys.stdin = open("input.txt", "r")

num = int(input())
g_cnt = 4


def f(num, cnt):
    global g_cnt
    #print(num, cnt)
    if num == 0:
        g_cnt = min(g_cnt, cnt)
        return
    if cnt > g_cnt:
        return
    for i in range(int(num**0.5), int((num//(4-cnt)) ** 0.5), -1):
        f(num - i**2, cnt+1)


f(num, 0)
print(g_cnt)
