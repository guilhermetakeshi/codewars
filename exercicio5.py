'''
Vamos considerar este exemplo (array escrito em formato geral):

ls = [0, 1, 3, 6, 10]

Suas seguintes partes:

ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []

As somas correspondentes são (juntas em uma lista): [20, 20, 19, 16, 10, 0]

A função parts_sums(ou suas variantes em outras linguagens) tomará como parâmetro uma lista ls 
e retornará uma lista das somas de suas partes conforme definido acima.

Outros exemplos:
ls = [1, 2, 3, 4, 5, 6] 
parts_sums(ls) -> [21, 20, 18, 15, 11, 6, 0]

ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
parts_sums(ls) -> [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]

Notas
- Dê uma olhada no desempenho: algumas listas possuem milhares de elementos.

'''
# 1 - somar os numeros da lista
# 2 - remover os numeros conforme aparecem e somar o restante da lista de numeros

def parts_sums(ls):
    sums = []           # Inicializa uma lista vazia para armazenar as somas parciais
    if not ls:          # Verifica se a lista de entrada é vazia
        return [0]      # Se for vazia, retorna uma lista contendo apenas 0

    sum_ls = sum(ls)     # Calcula a soma total de todos os elementos em ls
    sums.append(sum_ls)  # Adiciona a soma total à lista sums como a primeira soma

    for num in ls:
        sum_ls -= num  # Subtrai o elemento atual da soma acumulada
        sums.append(sum_ls)  # Adiciona a soma acumulada à lista sums

    return sums

ls = [1, 2, 3, 4, 5, 6]
resultado = parts_sums(ls)
print(resultado)
# [21, 20, 18, 15, 11, 6, 0]