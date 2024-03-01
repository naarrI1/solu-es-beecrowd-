hi, hf = map(int, input().split())

duracao = 0

if hi < hf:
    duracao = hf - hi
else:
    duracao = 24 - hi + hf

print(f'O JOGO DUROU {duracao} HORA(S)')