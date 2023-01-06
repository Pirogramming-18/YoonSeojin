def brGame() :
    num = 0
    gamePlay = True
    turn = 0
    attacker = None
    defender = None

    while gamePlay:
        if turn % 2 == 0:
            attacker = 'playerA'
            defender = 'playerB'
        else:
            attacker = 'playerB'
            defender = 'playerA'
        turn += 1
        
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
            print('{} : {}'.format(attacker, i))
            num += 1 
            if num == 31:
                gamePlay = False
                print('{} win!'.format(defender))
                break

if __name__ == "__main__":
    brGame()