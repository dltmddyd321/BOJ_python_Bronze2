import statistics
#숫자 데이터의 수학적 통계를 계산하는 함수 제공 

a, b, c = map(int, input().split())

mid = statistics.median([a,b,c])
#숫자 data의 중앙 값 반환 

print(mid)
