import sys
input = sys.stdin.readline
k = []

for i in range(7):
    a = int(input())
    if a%2 != 0:
        k.append(a)
if k:
    print(sum(k))
    print(min(k))
else:
    print(-1)
