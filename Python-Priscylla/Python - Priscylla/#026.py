frase = str(input("Digite uma frase: ")).upper().strip()

print("A letra A aparece {} na frase".format(frase.count("A")))
print("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
print("A última letra A apareceu na posição {}".format(frase.rfind("A")+1))




#frase = input("Digite uma frase: ")

#quantidade = frase.lower().count('a')

#prim = frase.lower().find('a') + 1  
#ulti = frase.lower().rfind('a') + 1  

#print(f"A letra 'A' aparece {quantidade} vezes na frase.")
#print(f"A primeira ocorrência da letra 'A' está na posição {prim}.")
#print(f"A última ocorrência da letra 'A' está na posição {ulti}.")