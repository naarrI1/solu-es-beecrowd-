hi, mi, hf, mf = map(int, input().split())

iniciomin = hi * 60 + mi
finalmin = hf * 60 + mf
duracaomin = (finalmin - iniciomin + 24 * 60) % (24 * 60)

if iniciomin == finalmin:
    duracaomin = 24 * 60

duracaohoras = duracaomin // 60
duracaominutos = duracaomin % 60

print(f'O JOGO DUROU {duracaohoras} HORA(S) E {duracaominutos} MINUTO(S)')