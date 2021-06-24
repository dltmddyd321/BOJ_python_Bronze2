res = int(input())

while True:
    cal = input()
    if cal == '=':
        break
    n= int(input())
    if cal == '+' :
        res += n
    elif cal == '-':
        res -= n
    elif cal == '*':
        res *= n
    elif cal == '/':
        res //= n
print(res)
