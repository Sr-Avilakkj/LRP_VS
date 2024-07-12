def ler_notas_alunos():
    alunos = {}
    while True:
        nome = input('Informe o nome do aluno (ou deixe vazio para terminar): ')
        if nome == '':
            break
        try:
            nota1 = float(input(f'Informe a primeira nota de {nome}: '))
            nota2 = float(input(f'Informe a segunda nota de {nome}: '))
        except ValueError:
            print('Nota inválida. Tente novamente.')
            continue
        alunos[nome] = (nota1, nota2)
    return alunos


def calcular_media(alunos, nome):
    if nome in alunos:
        notas = alunos[nome]
        media = sum(notas) / len(notas)
        return media
    else:
        return None


def main():
    alunos = ler_notas_alunos()
    while True:
        nome = input('Informe o nome do aluno para calcular a média (ou deixe vazio para terminar): ')
        if nome == '':
            break
        media = calcular_media(alunos, nome)
        if media is not None:
            print(f'A média de {nome} é {media:.2f}')
        else:
            print('Aluno não encontrado.')


if __name__ == '__main__':
    main()
