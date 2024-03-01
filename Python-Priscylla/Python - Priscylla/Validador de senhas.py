import re

def validar_senha(senha):
    if 6 <= len(senha) <= 32 and 
    re.match("^[A-Za-z0-9]*$", senha) and 
    any(c.isupper() for c in senha) and 
    any(c.islower() for c in senha) and 
    any(c.isdigit() for c in senha):
        return "Senha valida."
    else:
        return "Senha invalida."
while True:
    try:
        entrada = input()
        resultado = validar_senha(entrada)
        print(resultado)
    except EOFError:
        break