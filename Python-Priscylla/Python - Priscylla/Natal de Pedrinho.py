from datetime import datetime

while True:
    try:
        entrada = input().split()
        if not entrada:
            break

        mes, dia = map(int, entrada)
        natal = datetime(2016, 12, 25)
        data_atual = datetime(2016, mes, dia)

        if data_atual == natal:
            print("E natal!")
        elif (natal - data_atual).days == 1:
            print("E vespera de natal!")
        elif (natal - data_atual).days < 0:
            print("Ja passou!")
        else:
            print(f"Faltam {(natal - data_atual).days} dias para o natal!")

    except EOFError:
        break