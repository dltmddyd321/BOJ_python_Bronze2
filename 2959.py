import sys
nums = []

nums = sys.stdin.readline().strip().split(' ')
nums.sort(reverse = True)
#넓이가 가장 클 경우 직사각형은 두번째큰수 * 가장작은수의 식이다.
#크기가 큰 순으로 배치하기 위해 역으로 정렬.

print(int(nums[1])*int(nums[-1]))
