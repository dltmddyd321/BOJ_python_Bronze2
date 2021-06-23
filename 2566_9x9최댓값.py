max_num = 0

for i in range(9):
    row = list(map(int,input().split()))

    if max(row) > max_num:
        max_num = max(row) # 최댓값
        x = i + 1 #행(0번행부터라서 시각화할때는 +1)
        y = row.index(max_num) + 1 #열(인덱스가 0번부터 시작이라 +1)

print(max_num)
print(x,y)
