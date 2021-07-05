cock = list(map(int, input().split()))

odd_cock = []

for i in range(3):
    if cock[i] % 2 != 0:
        odd_cock.append(cock[i])
#홀수 값을 odd_cock 배열에 개별적으로 저장 

res = 1
if len(odd_cock) == 0:
    for i in range(3):
        res *= cock[i]

else:
    for i in range(len(odd_cock)):
        res *= odd_cock[i]

#홀수 값끼리 곱셈 

print(res)
