from math import factorial #팩토리얼 기능 import

n, k = map(int,input().split())

b = factorial(n)//(factorial(k)*factorial(n-k))
#이항 계수 계산 공식
print(b)
