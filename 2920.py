a = list(map(int, input().split()))

if a == sorted(a) : #sorted : 내림차순 정렬 
    print('ascending')
elif a == sorted(a, reverse=True): #역 순서라면 
    print('descending')
else :
    print('mixed')
