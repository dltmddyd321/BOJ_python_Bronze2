N, X = map(int, input().split())
A = list(map(int, input().split()))
#정수 수열이므로 map으로 형변환 후 list 생성

for i in range(N):
    if A[i] < X: #수열의 특정 요소가 정수 X보다 작다면 
        print(A[i], end=" ")
