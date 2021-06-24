while True:
    num = input()
    if num == "0":
        break
    res = len(num) + 1
    for n in num :
        if n=="0":
            res += 4
        elif n=="1":
            res += 2
        else:
            res += 3
    print(res)
