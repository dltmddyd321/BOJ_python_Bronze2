#1259 : 팰린드롬수

while True:
    n = input()

    if n == '0':
        break

    if n == n[::-1]:
        #n의 역순과 n이 같다면
        print('yes')
    else:
        print('no')
