def inteiros(n):
    return [int(input()) for _ in range(n)]

a = inteiros(5)
p = [300, 1500, 600, 1000, 150]
total = 225

for i in range(5):
    total += a[i] * p[i]


print(total)