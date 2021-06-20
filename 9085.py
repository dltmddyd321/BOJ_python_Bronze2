t = int(input())

for i in range(t):
    nums = [] #합계를 구하기 위한 배열 생성
    n = int(input())
    nums = sum(list(map(int,input().split())))
    print(nums)
