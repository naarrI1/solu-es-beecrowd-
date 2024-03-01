T = int(input())

for caso in range(1, T+1):
    
    escolha_sheldon, escolha_raj = input().split()
    
    if escolha_sheldon == escolha_raj:
       resultado = "De novo!"
    elif (escolha_sheldon == "tesoura" and 
    (escolha_raj == "papel" or escolha_raj == "lagarto")) or \
         (escolha_sheldon == "papel" and
         (escolha_raj == "pedra" or escolha_raj == "Spock")) or \
            (escolha_sheldon == "pedra" and 
         (escolha_raj == "lagarto" or escolha_raj == "tesoura")) or \
          (escolha_sheldon == "lagarto" and 
         (escolha_raj == "Spock" or escolha_raj == "papel")) or \
         (escolha_sheldon == "Spock" and (escolha_raj == "tesoura" or escolha_raj == "pedra")):
        resultado = "Bazinga!"
    else:
       resultado = "Raj trapaceou!"
        
    print(f"Caso #{caso}: {resultado}")
    