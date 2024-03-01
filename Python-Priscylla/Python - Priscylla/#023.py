num = int(input("Digite um número entre 0 e 9999: "))

u = num % 10
d = (num // 10) % 10
c = (num // 100) % 10
m = (num // 1000) % 10

print(f"Analisando o numero {num}")
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")    
    
    
#num = int(input("Digite um número entre 0 e 9999: "))

#if 0 <= num <= 9999:
    
#    unidade = num % 10
#    dezena = (num // 10) % 10
#    centena = (num // 100) % 10
#    milhar = (num // 1000) % 10
#    print(f"Unidade: {unidade}")
#    print(f"Dezena: {dezena}")
#    print(f"Centena: {centena}")
#    print(f"Milhar: {milhar}")
#else:
#    print("Número fora do intervalo permitido.")