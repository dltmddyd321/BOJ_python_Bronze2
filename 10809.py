S = list(map(str, input()))
#문자열 입력 

alpha = list('abcdefghijklmnopqrstuvwxyz')
#알파벳 리스트

array = [-1 for i in range(len(alpha))]
#알파벳 길이만큼 array에 -1

for i in range(len(S)):
    if array[alpha.index(S[i])] == -1:
        array[alpha.index(S[i])] = i
    #알파벳 리스트의 인덱스와 문자열 인덱스가 같으면 i

for j in array:
    print(j, end=" ")
    
