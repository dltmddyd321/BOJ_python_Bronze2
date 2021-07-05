N = int(input())

res = 0

for _ in range(N):
    a, b = map(int, input().split())
    res += b%a

print(res)
