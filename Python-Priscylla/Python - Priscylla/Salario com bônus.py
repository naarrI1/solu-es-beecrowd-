nome = input()
salario = float(input())
totalvendas = float(input())

comissao = totalvendas * 0.15

receber = salario + comissao

print(f"TOTAL = R$ {receber:.2f}")