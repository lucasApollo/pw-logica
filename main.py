nome = input("Digite seu nome:")
peso = float(input("Coloque aqui seu peso em Kg:"))
altura = float(input("Coloque aqui sua altura:"))

resultado = peso / (altura ** 2)

print(f"Olá {nome}, seu IMC é {resultado: .1f}:")