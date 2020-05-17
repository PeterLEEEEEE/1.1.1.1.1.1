import random


def randnum():
    num_list = []
    i = 0
    while i < 4:
        n = random.randint(0, 9)
        if n not in num_list:
            num_list.append(n)
            i+=1

    strl = ''.join(map(str, num_list))

    return strl

def Is_BallStrike(answer, guess):
    Ball = 0
    Strike = 0

    for i in range(4):
        for j in range(4):
            if guess[i]==answer[j]:
                if i == j:
                    Strike += 1
                else:
                    Ball += 1
    return Strike, Ball

playball = randnum()

count = 0
while True:
    count += 1
    play = input('{0}번째시도? '.format(count))
    if play == '0':
        print('안녕')
        break
    if play == playball:
        print('정답')
        break
    if count == 3:
        print('기회 끝')
        print('정답은 {0}입니다'.format(playball))
        break

    progress = Is_BallStrike(playball, play)
    print('%dS %dB' % progress)

