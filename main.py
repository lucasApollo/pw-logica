numero = int(input("Digite o número aqui:"))

pares = 0

impares = 0

for contador in range (1, numero + 1):

    if contador % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Quantidade de números pares {pares}")
print(f"Quantidade de números impares {impares}")