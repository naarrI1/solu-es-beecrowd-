codigo1, numero1, valor1 = map(float, input().split())

codigo, numero2, valor2 = map(float, input().split())

total = (numero1 * valor1) + (numero2 * valor2)

print(f"VALOR A PAGAR: R$ {total:.2f}")