from collections import Counter


def analisa_frequencia_de_letras(texto: str, n_frequencia: int):
    texto = Counter(list(texto.lower()))
    lista = list()

    for letra, frequencia in texto.items():
        total = sum(texto.values())
        porcentagem = (frequencia*100/total).__round__(0)
        tupla = (letra, porcentagem)
        lista.append(tupla)

    dicionario = dict(lista)
    mais_comum = Counter(dicionario).most_common(n_frequencia)
    for elemento, proporcao in mais_comum:
        print(f'{elemento} ==> {proporcao}%')
