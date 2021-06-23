N = int(input())

sq = [2**i for i in range(31)]

if N in sq :
    print(1)
else:
    print(0)
