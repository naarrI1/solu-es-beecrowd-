from math import sqrt

cateOP = float(input("Digite o comprimento do cateto oposto: "))
cateAD = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = sqrt(cateOP**2 + cateAD**2)

print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")