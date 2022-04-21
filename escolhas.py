from historia import bifurcacao_1, bifurcacao_2


def escolha_1():
    opcao = int(input('Primeira escolha: '))
    if opcao == 1:
        return True
    else:
        print('A garota fica com medo de desobecer seus pais e decide obedece-los. Continuando sua vida no interior...\n Fim.')
        exit()


def escolha_2():
    opcao = int(input('Segunda escolha: '))
    if opcao == 1:
        bifurcacao_1()
    else:
        bifurcacao_2()
