from historia import introducao, part_1, part_2


def apresentacao():
    print('BEM-VINDO jogador. \nEste é um jogo curto de escolhas.')
    print('+-------------+')
    print('| 1 - Iniciar |')
    print('| 2 - Sinopse |')
    print('| 3 - Sair    |')
    print('+-------------+')


def menu():
    opcao = int(input('Escolha: '))
    if opcao == 1:
        inicia()
    elif opcao == 2:
        introducao()
        inicia()
    else:
        print('Saindo..')


def inicia():
    part_1()
    part_2()


apresentacao()
menu()
