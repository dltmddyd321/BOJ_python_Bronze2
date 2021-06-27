n = int(input())
hap = 0
res = 0

k = list(map(int, input().split()))

for i in range(n) :
    if k[i] == 1 :
        hap += 1
        res += hap
    else :
        hap = 0

print(res)
