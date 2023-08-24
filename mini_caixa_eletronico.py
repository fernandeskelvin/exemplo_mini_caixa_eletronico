def mostrar_menu():
    print('\nMenu de operação\n')
    print('[a] Mostrar Saldo')
    print('[b] Efetuar Depósito')
    print('[c] Efetuar Saque')
    print('[d] Finalizar\n')
    opcao_selecionada = input('Digite uma opção: ')
    return opcao_selecionada

saldo = 0
encerrar_programa = False

while encerrar_programa != True:
    opcao_selecionada = mostrar_menu()
    if opcao_selecionada == 'a':
        print('Seu saldo é:', saldo)
    elif opcao_selecionada == 'b':
        deposito = int(input('Digite o valor a depositar: '))
        saldo = saldo + deposito
        print('Depósito efetuado')
    elif opcao_selecionada == 'c':
        retirada = int(input('Digite valor a retirar: '))
        if retirada > saldo:
            print('Saque não permitido, saldo insuficiente')
        else:
            saldo = saldo - retirada
            print('Saque efetuado')
    elif opcao_selecionada == 'd':
        encerrar_programa = True
    else:
        print('Opção inválida, tente novamente')