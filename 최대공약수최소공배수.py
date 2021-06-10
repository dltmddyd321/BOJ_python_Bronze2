a, b = map(int, input().split())
 
def gcd(a, b): # 최대공약수
    while b != 0:
        c = a%b
        a = b
        b = c
    return a
 
def lcm(a,b): # 최소공배수
    baesu = (a*b) / gcd(a,b)
    return baesu
 
print(gcd(a,b))
print(int(lcm(a,b)))

#유클리드 호제법 : 두 자연수 a,b 에서 (a>b) a를 b로 나눈
#나머지를 r이라 하면, a,b의 최대공약수는 b와 r의 최대공약수와 같다.
#따라서 a에 b를 넣고, b에 r을 넣고 나머지가 0이 될 때까지 반복
#이때 a가 최대공약수가 된다.
#최소공배수는 두 수를 곱해서 최대공약수로 나누면 된다. (/)
