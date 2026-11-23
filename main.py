while True:

    print("___Calculadora___\n"
    "1- Somar \n"
    "2- Subtrair \n"
    "3- Multiplicar \n"
    "4- Dividir \n"
    "5- Sair \n")

    opcao = int(input("Escolha uma opção:"))

    if opcao == 4:
        print("Você escolheu Dividir")
        break

    if opcao == 1:
        print("Você escolheu Somar")
        break
    
    elif opcao == 2:
        print("Você escolheu Subtrair")
        break
    
    elif opcao == 3:
        print("Você escolheu Multiplicar")
        break
    else:
        print("Opção invalida")