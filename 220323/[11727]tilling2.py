import sys
sys.stdin = open("input.txt", "r")


list = [1, 3]

for i in range(1000):
    list.append(list[-1] + list[-2]*2)

print(list[int(input())-1]%10007)
