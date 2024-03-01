import math

angulo = float(input("Digite o valor do ângulo em graus: "))

angulo = math.radians(angulo)

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")