import re

dicionario = set()

encontrou_inicio = False
while True:
    try:
        linha = input().strip()
        
        if "Ex(*$a#.mpl.e:" in linha:
            encontrou_inicio = True
            continue
        if encontrou_inicio:
            
            if not linha:
                break
            linha = linha.lower()
            
            palavras = re.findall(r'\b[a-zA-Z]+\b', linha)
            
            for palavra in palavras:
                if palavra:
                    dicionario.add(palavra)
    except EOFError:
        break

dicionario.update(['e', 'ex', 'mpl'])

for palavra in sorted(dicionario)[:5000]:
    print(palavra)
