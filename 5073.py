while True:
    a,b,c = map(int,input().split())
    if a+b+c == 0:
        break

    list=[a,b,c]
    if sum(list) <= max(list)*2 :
        print('Invalid')
    elif a==b==c :
        print('Equilateral')
    elif a==b or a==c or b==c :
        print('Isosceles')
    else :
        print('Scalene')
