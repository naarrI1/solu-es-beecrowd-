T = int(input())

for caso in range(1, T+1):
    
    escolha_rajesh, escolha_sheldon = input().split()
    
    escolha_rajesh = escolha_rajesh.lower().strip()
    escolha_sheldon = escolha_sheldon.lower().strip()
    
    if escolha_rajesh == escolha_sheldon:
        resultado = "empate"
    elif (escolha_rajesh == "tesoura" and 
          (escolha_sheldon == "papel" or escolha_sheldon == "lagarto")) or \
         (escolha_rajesh == "papel" and
          (escolha_sheldon == "pedra" or escolha_sheldon == "spock")) or \
         (escolha_rajesh == "pedra" and 
          (escolha_sheldon == "lagarto" or escolha_sheldon == "tesoura")) or \
         (escolha_rajesh == "lagarto" and 
          (escolha_sheldon == "spock" or escolha_sheldon == "papel")) or \
         (escolha_rajesh == "spock" and 
          (escolha_sheldon == "tesoura" or escolha_sheldon == "pedra")):
        resultado = "rajesh"
    else:
        resultado = "sheldon"
        
    print(resultado)