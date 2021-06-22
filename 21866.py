max_score = [100, 100, 200, 200, 300, 300, 400, 400, 500]

score = list(map(int,input().split()))

hacker = False #해커의 판명 여부를 결정지을 상태 변수

sum = 0 #합계 점수를 담을 변수

for i in range(len(score)) :
    if score[i] > max_score[i]:
        hacker = True
        break
    else:
        sum+=score[i]

if hacker:
    print('hacker')
else :
    if sum>= 100:
        print('draw')
    else:
        print('none')
