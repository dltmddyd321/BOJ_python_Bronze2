t = int(input())

for i in range(t):
    num, s = input().split()
    num = int(num)
    s = str(s)
    for i in range(len(s)):
        print(num*s[i], end='') #한 워드당 지정 개수만큼 반복 출력 
    print()
    
