import random
from time import sleep
totj = 0
totc = 0
tote = 0
print('\033[36m-=' * 20)
print('\033[1;35m         SUPER JOKENPO DO MAIATE\033[m')
print('\033[36m-=' * 20)
j = 'a'
while True:
    ppt = ['Pedra', 'Papel', 'Tesoura']
    j = input('\033[32mPedra, Papel ou Tesoura? ').strip().title()
    c = random.choice(ppt)
    if j == 'Pedra' or j== 'Papel' or j== 'Tesoura':
        print('\033[1;34m                   JO')
        sleep(1)
        print('\033[1;34m                   KEN')
        sleep(1)
        print('\033[1;34m                   PO!!!')
        sleep(1)
    if j == 'Papel' and c == 'Tesoura' or j == 'Pedra' and c == 'Papel' or j == 'Tesoura' and c == 'Pedra':
        print('\033[31m-=' * 27)
        print('\033[33mO Computador escolheu {} e você escolheu {}.\n'
              '   \033[1;31m              VOCÊ PERDEU!\033[m'.format(c, j))
        totc += 1
        print('\033[31m-=\033[m' * 27)
    elif c == 'Papel' and j == 'Tesoura' or c == 'Pedra' and j == 'Papel' or c == 'Tesoura' and j == 'Pedra':
        print('\033[31m-=' * 27)
        print('\033[33mO Computador escolheu {} e você escolheu {}.\n'
              '    \033[34m             VOCÊ GANHOU!'.format(c, j))
        totj += 1
        print('\033[31m-=\033[m' * 27)
    elif j == c:
        print('\033[33mVocês empataram, tente novamente\033[m')
        tote += 1
    else:
        print('\033[1;31mDIGITE APENAS: PEDRA, PAPEL OU TESOURA!\033[m\U0001F621')
    cont = ' '
    while cont not in 'SN':
        cont = str(input('\033[32mVocê quer continuar? [S/N] ')).strip().upper()[0]
        if cont not in "SN":
            print('\033[1;31mDIGITE APENAS SIM OU NÃO 😡\033[m')
    if cont == 'N':
        break

print('\033[35m-=' * 30)
print('\033[34m                         PLACAR DO JOGO')
print(f'\033[33m[{totc}]\033[34m Computador            \033[33m[{totj}]\033[34m Jogador         \033[33m[{tote}]\033[34m Empate')
print('\033[35m-=' * 30)
print('\033[33m                           Fim de jogo!')


