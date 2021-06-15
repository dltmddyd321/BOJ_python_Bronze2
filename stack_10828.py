import sys
n = int(sys.stdin.readline())
#시간초과 에러 방지를 위해 import

stack = []
for i in range(n):
    menu = sys.stdin.readline().split()

    if menu[0] == 'push':
        stack.append(menu[1])
    elif menu[0] == 'pop':
        if len(stack) == 0:
            #스택에 현재 자료가 없다면(길이가 0)
            print(-1)
        else:
            print(stack.pop())
    elif menu[0] == 'size' :
        print(len(stack))
    elif menu[0] == 'empty' :
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif menu[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
