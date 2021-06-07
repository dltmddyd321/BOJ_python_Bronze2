word = input().lower() #소문자로 바꿔주는 함수
word_list = list(set(word)) #set : 중복 제거 함수
cnt = [] #가장 많이 사용된 알파벳을 저장하기 위한 리스트

for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else :
    print(word_list[(cnt.index(max(cnt)))].upper())
    #upper : 대문자로 변경 
