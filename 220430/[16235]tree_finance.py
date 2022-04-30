import sys
sys.stdin = open("input.txt", "r")

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
tree_age = [[0] * N for _ in range(N)]
tree_true = [[0] * N for _ in range(N)]  # 칸에 나무 몇 개 있는지
Map = [[5]*N for _ in range(N)]


def spring():
    for y in range(N):
        for x in range(N):
            if tree_true[y][x] > 0:  # 나무가 하나라도 있으면
                if len(tree_age[y][x]) == 1:  # 트리가 하나만 있는 경우
                    if tree_age[y][x] > Map[y][x]:  # 양분이 나이보다 적을 경우
                        tree_age[y][x] = 1
                        tree_true[y][x] = 0
                    else:
                        Map[y][x] -= tree_age[y][x]
                        tree_age += 1
                elif len(tree_age[y][x]) > 1:  # 한 개 이상일 경우
                    temp_list = tree_age[y][x].sort()
                    temp_tree_true = 0
                    for i in temp_list:
                        if i > Map[y][x]:
                            break
                        else:
                            Map[y][x] -= 1
                            temp_tree_true += 1
                            i += 1
                    tree_true[y][x] = temp_tree_true
                    tree_age[y][x] = temp_list


def summer():
    pass


def fall():
    pass


def winter():
    pass


for _ in range(M):
    r, c, age = map(int, input().split())
    tree_age[r-1][c-1] = age
    tree_true[r-1][c-1] += 1
