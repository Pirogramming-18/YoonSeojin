num = 0

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

gameCount = 1
for i in range(num+1, playN+1):
    print('playerA : {}'.format(i))
    gameCount += 1

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

for i in range(gameCount+1, gameCount+playN+1) : 
    print('playerB : {}'.format(gameCount))
    gameCount += 1