T = int(input())

for i in range(T) :
    input_nums = list(map(int,input().split()))
    even_nums = [] #짝수를 담을 리스트

    for i in input_nums :
        if i%2 == 0:
            even_nums.append(i)

    print(sum(even_nums), min(even_nums))

    
