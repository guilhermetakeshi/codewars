# exercicio para verificar se a palavra é um isograma

def is_isogram(string):
    string = string.upper().strip()
    # metododos usados para que todas as letras sejam maiúsculas e para 
    # remover quaisquer espaços em branco
    repetition = []
    
    for letter in string:
        if letter not in repetition:
            repetition.append(letter)
    # Se a letra não estiver na lista, ela é adicionada à lista "repetition" 
    # usando o método "append()"
        else:
            return False
    # Se a letra já estiver na lista, isso significa que a letra foi repetida na string, 
    # e a função retorna False, indicando que a string não é um isograma.
    return True
    
    # Se o loop for concluído sem retornar False, isso significa que a string não possui 
    # letras repetidas e a função retorna True, indicando que a string é um isograma.

print(is_isogram('Dermatoglyphics'))

'''
melhor jeito de fazer:

def is_isogram(string):
    return len(string) == len(set(string.lower()))


print(is_isogram('Dermatoglyphics'))

'''