score = []

for i in range(5):
    score.append(sum(map(int,input().split())))
    # for문을 5번 돌면서 입력되는 즉시 각 점수의 합계를 누적 

print(score.index(max(score))+1, max(score))
#인덱스값이 0번부터 시작하므로 우승자 번호 출력 시 +1 해줌
#최대 값을 가진 인덱스를 추출 
