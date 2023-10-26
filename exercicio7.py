'''
Escreva uma função chamada first_non_repeating_letterque recebe uma string 
de entrada e retorna o primeiro caractere que não é repetido em nenhum lugar da string.

Por exemplo, se for dada a entrada 'stress', a função deverá retornar 't', 
já que a letra t ocorre apenas uma vez na string e ocorre primeiro na string.

Como um desafio adicional, letras maiúsculas e minúsculas são consideradas o 
mesmo caractere , mas a função deve retornar a caixa correta para a letra 
inicial. Por exemplo, a entrada 'sTreSS'deve retornar 'T'.

Se uma string contiver todos os caracteres repetidos , ela deverá retornar uma
string vazia ( "") ou None- veja exemplos de testes.

1- Inicialize um dicionário para contar a frequência de cada caractere na string.
2- Percorra a string para contar a frequência de cada caractere e armazenar no dicionário.
3- Percorra a string novamente e verifique a frequência de cada caractere no dicionário.
4- Assim que encontrar o primeiro caractere com frequência 1, retorne esse caractere.
5- Certifique-se de tratar letras maiúsculas e minúsculas como equivalentes, conforme especificado.
'''
def first_non_repeating_letter(s):
    # Inicialize um dicionário para contar a frequência de cada caractere, considerando letras maiúsculas e minúsculas como equivalentes
    char_count = {}

    # Passo 1: Contar a frequência de cada caractere na string
    for char in s:
        # Use o caractere em letra minúscula para contar
        char_lower = char.lower()
        if char_lower in char_count:
            char_count[char_lower] += 1
        else:
            char_count[char_lower] = 1

    # Passo 2: Encontrar o primeiro caractere não repetido
    for char in s:
        char_lower = char.lower()
        if char_count[char_lower] == 1:
            return char  # Retorne o caractere original

    # Passo 3: Se nenhum caractere não repetido for encontrado, retornar uma string vazia
    return ''

# Exemplos de uso:
print(first_non_repeating_letter('stress'))  # Deve retornar 't'
print(first_non_repeating_letter('sTreSS'))  # Deve retornar 'T'
print(first_non_repeating_letter('abba'))    # Deve retornar ''
