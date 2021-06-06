a = int(input())
b = int(input())
c = int(input())

result = list(str(a*b*c))
#각 요소의 개수를 반환하기 위해 str, list 형으로 변환 
for i in range(10):
    print(result.count(str(i)))
#문자열 내부에서 특정 문자, 혹은 문자열의 개수를 반환하는 함수 count()
