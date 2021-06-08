A, B, V = map(int, input().split())

dis_high = V - A
#잔여 거리를 계산 

if dis_high % (A-B) == 0:
    day = int(dis_high/(A-B)) #나누어 떨어지면 +1 없음  
else :
    day = int(dis_high/(A-B) + 1) #초과값으로 인해 1일 추가 
print(day + 1)
