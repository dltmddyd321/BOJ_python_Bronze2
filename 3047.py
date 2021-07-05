num = list(map(int, input().split()))
order = input()
num = sorted(num)
#기본 오름차순 정렬

for i in order:
    if i == 'A':
        print(num[0], end = ' ')
    elif i == 'B':
        print(num[1], end = ' ')
    elif i == 'C':
        print(num[2], end = ' ')
