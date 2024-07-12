def ler_tempos():
    corredores = {}
    for _ in range(6):
        nome = input('Digite o nome do corredor: ')
        tempos = []
        for volta in range(10):
            tempo = float(input(f'Digite o tempo da volta {volta + 1} do corredor {nome}: '))
            tempos.append(tempo)
        corredores[nome] = tempos
    return corredores


def melhor_volta(corredores):
    melhor_tempo = float('inf')
    melhor_corredor = None
    melhor_volta = None

    for corredor, tempos in corredores.items():
        for i, tempo in enumerate(tempos):
            if tempo < melhor_tempo:
                melhor_tempo = tempo
                melhor_corredor = corredor
                melhor_volta = i + 1

    return melhor_corredor, melhor_volta, melhor_tempo


def classificacao_final(corredores):
    medias = {}
    for corredor, tempos in corredores.items():
        medias[corredor] = sum(tempos) / len(tempos)

    return sorted(medias.items(), key=lambda item: item[1])


def main(melhor_volta):
    corredores = ler_tempos()

    melhor_corredor, melhor_volta, melhor_tempo = melhor_volta(corredores)
    print(f'\nA melhor volta foi do corredor {melhor_corredor}, na volta {melhor_volta}, '
          f'com o tempo de {melhor_tempo:.2f} segundos.')

    classificacao = classificacao_final(corredores)
    print('\nClassificação final:')
    for i, (corredor, media) in enumerate(classificacao):
        print(f'{i + 1}º lugar: {corredor} com média de {media:.2f} segundos.')


if __name__ == '__main__':
    main(melhor_volta)
    