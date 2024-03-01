nome = str(input("Digite o nome completo: ")).strip()

maiusculo = nome.upper()
minusculo = nome.lower()
print("analisando seu nome...")
print(f"Seu nome em maiúsculo é: {maiusculo}")
print(f"Seu nome em minúsculo é: {minusculo}")
print("Seu nome tem ao todo {} letras".format(len(nome)- nome.count(" ")))
print("seu primeiro nome tem {} letras".format(nome.find(" ")))