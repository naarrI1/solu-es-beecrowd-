valor = float(input())
centavos = int(valor * 100)

notas_moedas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]

quantidades = {}

print("NOTAS:")
for nota_moeda in notas_moedas[:6]:
    quantidade = centavos // (nota_moeda * 100)
    centavos %= nota_moeda * 100
    print(f"{quantidade} nota(s) de R$ {nota_moeda:.2f}")

print("MOEDAS:")
for nota_moeda in notas_moedas[6:]:
    quantidade = centavos // int(nota_moeda * 100)
    centavos %= int(nota_moeda * 100)
    print(f"{quantidade} moeda(s) de R$ {nota_moeda:.2f}")