def risada(r):
    vogais = set('aeiou')
    risnotconso = ''.join(letra for letra in r if letra in vogais)
    return "S" if risnotconso == risnotconso [::-1] else "N"

risinput = input().strip()

print(risada(risinput))