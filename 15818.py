n, m = map(int,input().split())

k = list(map(int, input().split()))

res = 1

for i in k:
    res *= i

print(res%m)
