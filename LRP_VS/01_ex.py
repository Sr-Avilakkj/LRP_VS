def vowels_counter(text):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    consonants = {'b': 0, 'c': 0, 'd': 0, 'f': 0, 'g': 0, 'h': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
                  'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    not_vowels_or_consonants = 0

    for letra in text.lower():
        if letra in vowels:
            vowels[letra] += 1
        elif letra in consonants:
            consonants[letra] += 1
        else:
            not_vowels_or_consonants += 1

    return vowels, consonants, not_vowels_or_consonants


text = input('Informe o texto para a análise:\n')
vowels, consonants, not_vowels_or_consonants = vowels_counter(text)
print(f'Vogais:\n{vowels}')
print(f'Consoantes:\n{consonants}')
print(f'A quantidade de elementos que não são vogais ou consoantes foi de: {not_vowels_or_consonants}')
