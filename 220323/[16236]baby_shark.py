import sys
from collections import deque

sys.stdin = open("input.txt", "r")
N = int(input())

Map = [list(map(int, input().split())) for _ in range(N)]
baby_shark_size = 2
baby_full = 0
baby_shark_y, baby_shark_x = 0, 0
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]
sec = 0
fish_list = []
min_Map_dis = [[0]*N for _ in range(N)]

def init():
    global fish_list, min_Map_dis
    fish_list = []
    min_Map_dis = [[0]*N for _ in range(N)]

def baby_shark_pos():
    global baby_shark_y, baby_shark_x
    for y in range(N):
        for x in range(N):
            if Map[y][x] == 9:
                baby_shark_y, baby_shark_x = y, x
                return 0

def mom_shark_help():
    for y in range(N):
        for x in range(N):
            if 0 < Map[y][x] < baby_shark_size:
                return 0
    else :
        return 1

def check_fish():
    for y in range(N):
        for x in range(N):
            if 0 < Map[y][x] < baby_shark_size:
                fish_list.append([y, x, Map[y][x]])

def dfs():
    for y in range(N):
        for x in range(N):
            if y == baby_shark_y and x == baby_shark_x :
                continue
            else:
                if Map[y][x] > baby_shark_size :
                    min_Map_dis[y][x] = -1

    dfs_list = deque([[baby_shark_y, baby_shark_x]])
    while(dfs_list):
        yy, xx = dfs_list.popleft()
        for i in range(4):
            yyy = yy + dy[i]
            xxx = xx + dx[i]
            if N> yyy >= 0 and N > xxx >= 0 and Map[yyy][xxx] != -1:
                if yyy == baby_shark_y and xxx == baby_shark_x:
                    continue
                if(min_Map_dis[yyy][xxx] == 0) :
                    min_Map_dis[yyy][xxx] = min_Map_dis[yy][xx] + 1
                    dfs_list.append([yyy, xxx])

def catch_fish():
    global sec, baby_shark_size, baby_full 
    min_dis, min_y, min_x = 21e8, 0, 0
    if len(fish_list) == 1:
        min_y, min_x = fish_list[0][0], fish_list[0][1]
        min_dis = min_Map_dis[min_y][min_x]
        if min_dis == 0:
            print(sec)
            return 1
    else:
        for i in range(len(fish_list)):
            if min_Map_dis[fish_list[i][0]][fish_list[i][1]] == 0:
                continue
            if min_dis > min_Map_dis[fish_list[i][0]][fish_list[i][1]]:
                min_y, min_x = fish_list[i][0], fish_list[i][1]
                min_dis = min_Map_dis[min_y][min_x]
    if min_dis > 21e7:
        print(sec)
        return 1
    sec += min_dis
    baby_full += 1
    if baby_full == baby_shark_size :
        baby_shark_size += 1
        baby_full = 0
    Map[min_y][min_x] = 9
    Map[baby_shark_y][baby_shark_x] = 0


while(1):
    init()
    baby_shark_pos() # 아기 상어 위치 체크
    if mom_shark_help() : # 먹을 수 있는 물고기 유무 체크
        print(sec)
        break

    check_fish() # 먹을 수 있는 물고기 fish_list에 담기
    dfs()
    # for i in min_Map_dis:
    #     print(i)
    # print()
    if catch_fish() : break
    # for i in Map:
    #     print(i)
    # print("===")
    # print()