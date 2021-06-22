T = int(input())

s = list(map(int,input().split()))
y = 0
m = 0
for i in s :
    y += i//30*10 + 10
    m += i//60*15 + 15
    #30초 마다 10원씩 청구된다고 하면 x가 통화시간일때
    #x에 30을 나눈 몫에 10을 곱하고 10을 더하면 답.
    #60초마다 15원씩 청구되는 것도 마찬가지.
if y<m:
    print('Y %d' % y)
elif y > m:
    print('M %d' % m)
else :
    print('Y M %d' % y)
    
