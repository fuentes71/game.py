from apres_decisoes import decisao_3


def bi_escolha_1():
    contador = 0
    while True:
        opcao = int(input('Escolha: '))
        if opcao == 1:
            if contador == 0:
                print('Sem forças para continuar, continua ali bebendo..')
                decisao_3()
            elif contador == 1:
                print(
                    'Ela chorano pelas suas decisões continua bebendo mais e mais..')
                decisao_3()
            elif contador == 2:
                print(
                    'Depois de tanto beber ela acaba tendo uma overdose e por estar em um local isolado, ninguém vê o que está acontecendo e acaba morrendo. Fim')
                exit()
        else:
            break
        contador += 1
    print('trocou')
