n = int(input())
num = int(input())

while num:
    if num == 0 :
        break
    elif num%n == 0:
        print("%s is a multiple of %s." % (num, n))
    else :
        print("%s is NOT a multiple of %s." % (num, n))
    num = int(input())
    
