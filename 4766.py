t1 = float(input())

while True:
    t2 = float(input())
    if t2 == 999:
        break
    print("%.2f" % (t2-t1))
    t1 = t2 #다음 계산을 위해 물려받음 
