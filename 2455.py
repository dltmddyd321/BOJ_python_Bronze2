plp_nums = []
plp = 0

for _ in range(4) :
    out_num, in_num = map(int,input().split())
    plp += in_num
    plp -= out_num


    plp_nums.append(plp)

print(max(plp_nums))
