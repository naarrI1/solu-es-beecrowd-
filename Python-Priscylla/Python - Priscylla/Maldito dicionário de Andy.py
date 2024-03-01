import re

dicionario = set()

try:
    while True:
        linha = input().strip()
        
        if re.search(r'\b[a-zA-Z]+\b', linha):
            
            linha = linha.lower()
            
            palavras = re.findall(r'\b[a-zA-Z]+\b', linha)
            
            for palavra in palavras:
                if palavra:
                    dicionario.add(palavra)
except EOFError:
    pass

for palavra in sorted(dicionario)[:5000]:
    print(palavra)