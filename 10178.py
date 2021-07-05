T = int(input())

for _ in range(T):
    n, m = map(int,input().split())
    print("You get {0} piece(s) and your dad gets {1} piece(s).".format(n//m, n%m))
