class Etiqueta:
    def __init__(self, lingua, traducao):
        self.lingua = lingua
        self.traducao = traducao

def procura_traducao(etiquetas, idioma):
    for i, etiqueta in enumerate(etiquetas):
        if etiqueta.lingua == idioma:
            return i

if __name__ == "__main__":
    qts_traducoes = int(input())

    etiquetas = []
    for _ in range(qts_traducoes):
        lingua = input()
        traducao = input()
        etiquetas.append(Etiqueta(lingua, traducao))

    qts_criancas = int(input())

    for _ in range(qts_criancas):
        crianca = input()
        idioma = input()

        idx_traducao = procura_traducao(etiquetas, idioma)
        print(f"{crianca}\n{etiquetas[idx_traducao].traducao}\n")