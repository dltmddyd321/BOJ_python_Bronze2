nmg = []
#42로 나눈 값을 리스트 형식으로 저장한다.

for i in range(10) :
    num = int(input())
    nmg.append(num%42)
    #append : 배열에 num을 42로 나눈 나머지값을 저장한다.

nmg = set(nmg)
print(len(nmg))
#set을 통해 중복되지 않는 집합을 생성하고 그 집합 배열의 길이를 구한다.
