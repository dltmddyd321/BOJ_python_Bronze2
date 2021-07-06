for _ in range(int(input())):
    N = int(input())
    k = sorted(map(int, input().split()))
    print(k[0], k[-1])
