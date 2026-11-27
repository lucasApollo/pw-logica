notas = []
soma = 0
for contador in range(5):
    nota = float(input(f"Digite a {contador + 1}ª nota: "))
    notas.append(nota)
    soma += nota

media = soma / len(notas)

print(f"A soma de todas as notas é: {soma}")
print(f"As médias das notas é: {media}")
print("Maior nota: ", max(notas))
print("Menor nota: ", min(notas))
