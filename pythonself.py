import random
RSP = ('가위', '바위', '보')
player = ('컴A', '컴B', '컴C', '컴D', '당신')
hand = ['', '', '', '', '']
win_hand = []
while True: # 가위바위보 선택
    for i in range(4):
        hand[i] = random.choice(RSP)
    hand[4] = input('가위-바위-보? ')
    if (hand[4] not in RSP):
        print('안녕!')
        break

    print('%s: %s' % (player[0], hand[0]), end='')
    for i in range(1, 4):
        print(', %s: %s' % (player[i], hand[i]), end='')
    print()
# 승자 분석
    num_hand = {'가위': 0, '바위': 0, '보': 0}
    for i in range(5):
        num_hand[hand[i]] += 1

    if num_hand['가위'] == 5 or num_hand['바위'] == 5 or num_hand['보'] == 5:
        print('서로 비겼습니다.')
    elif num_hand['가위'] > 0 and num_hand['바위'] > 0 and num_hand['보'] > 0:
        print('서로 비겼습니다.')
    else:
        if num_hand['가위'] == 0:     # 가위가 없으면,
            win_hand = '보'           # 바위-보 중에 보가 승리
        elif num_hand['바위'] == 0:   # 바위가 없으면,
            win_hand = '가위'         # 가위-보 중에 가위가 승리
        else:                         # 보가 없으면,
            win_hand = '바위'         # 가위-바위 중에 바위가 승리
# 승자 출력
    winner = []
    for i in range(5):
        if hand[i] == win_hand:
            winner += [player[i]]

    print(winner[0], end='')
    for i in range(1, len(winner)):
        print(',', winner[i], end='')
        if winner[-1] == '당신':
            print('이 이겼습니다.')
        else:
            print('가 이겼습니다.')
    print()