opcao = 0
while opcao != 4:
    print("\n=====Menu de Operações=====")
    print("1 - Mostrar mesnagem de Boas-Vindas!")
    print("2 - Mostrar a tabuada de um número")
    print("3 - Informar se um número é par ou ímpar")
    print("4 - Sair")
    opcao = int(input("Escolher uma opção: "))

    if opcao == 1:
        print("\nSeja Bem-Vindo")
    elif opcao == 2:
        numero = int(input(
            "Digite um número para ver a tabuada do próprio: "))
        for contador in range(1, 11):
            print(f"{numero} X {contador} = {numero * contador}")

    elif opcao == 3:
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            print(f"O Seu número {numero} é PAR!")
        else:
            print(f"O seu número {numero} é ÍMPAR!")
    elif opcao == 4:
        print("\n Encerrando o painel... Até mais!")
    else: 
        print("Opção invalida")