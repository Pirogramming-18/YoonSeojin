num = 0
gamePlay = True

while gamePlay:
    #PlayerA
    while True:
        try:
            playN = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
            if playN == 1 or playN == 2 or playN == 3:
                break
            else:
                print('1,2,3 중 하나를 입력하세요')
                continue
        except ValueError as e:
            print('정수를 입력하세요')

    for i in range(num+1, num+playN+1): 
        print('playerA : {}'.format(i))
        num += 1 
        if num == 31:
            gamePlay = False
            print('palyerB win!')
            break

    #playerB
    while True:
        try:
            playN = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
            if playN == 1 or playN == 2 or playN == 3:
                break
            else:
                print('1,2,3 중 하나를 입력하세요')
                continue
        except ValueError as e:
            print('정수를 입력하세요')

    for i in range(num+1, num+playN+1) : 
        print('playerB : {}'.format(i))
        num += 1
        if num == 31:
            gamePlay = False
            print(print('palyerA win!'))
            break