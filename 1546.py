n = int(input())

sum_score = 0

score = list(map(int,input().split()))
max_score = max(score) #리스트의 최댓값

for i in range(n) :
    score[i] = score[i]/max_score*100
    sum_score += score[i]

avg = sum_score / n
print(avg)
