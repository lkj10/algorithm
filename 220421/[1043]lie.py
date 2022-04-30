import sys
sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())
linked = [0]*(N+1)
true_list = list(map(int, input().split()))
for i in range(1, len(true_list)):
    linked[true_list[i]] = 1
all_list = []
for _ in range(M):
    party_list = list(map(int, input().split()))
    all_list.append(party_list)
for i in all_list:
    check = 0
    for k in range(i[0]):
        if linked[i[k+1]] == 1:
            check = 1
    if check == 1:
        for k in range(i[0]):
            linked[i[k+1]] = 1

answer = M

for i in all_list:
    for k in range(i[0]):
        if linked[i[k+1]] == 1:
            answer -= 1
            break

print(answer)
