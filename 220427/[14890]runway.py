import sys
sys.stdin = open("input.txt", "r")

N, L = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def foo(List):
    for x in range(N-1):
        if abs(List[x] - List[x+1]) > 1:
            return False
        if List[x] < List[x+1]:  # 오른쪽이 더 클 경우
            for z in range(x, x-L, -1):
                if z < 0 or visit[z] or List[z] != List[x]:
                    return False
                if List[x] == List[z]:
                    visit[z] = 1
        elif List[x] > List[x+1]:  # 왼쪽이 더 클 경우
            for z in range(x+1, x+L+1):
                if z >= N or visit[z] or List[z] != List[x+1]:
                    return False
                if List[x+1] == List[z]:
                    visit[z] = 1
    return True


for y in range(N):  # 가로 체크
    visit = [False for _ in range(N)]
    if foo(Map[y]):
        answer += 1

visit = [[0]*N for _ in range(N)]
# 해당 부분에 이미 사다리 설치되어있는지 확인 필요
for x in range(N):  # 세로 체크
    visit = [False for _ in range(N)]
    if foo(list(Map[y][x] for y in range(N))):
        answer += 1

print(answer)
