while True:
    try :
        print(input())
    except EOFError:
        #Ctrl로 인한 입력 오류 방지
        break
