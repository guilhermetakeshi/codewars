'''
1, 246, 2, 123, 3, 82, 6, 41são os divisores do número 246. Elevando ao quadrado 
esses divisores obtemos: 1, 60516, 4, 15129, 9, 6724, 36, 1681. A soma desses 
quadrados é 84100qual é 290 * 290.

Tarefa
Encontre todos os inteiros entre me n(m e n inteiros com 1 <= m <= n) de modo que a soma 
de seus divisores quadrados seja ela mesma um quadrado.

Retornaremos um array de subarrays ou de tuplas (em C um array de Pair) ou uma string. 
As submatrizes (ou tuplas ou pares) terão dois elementos: primeiro o número cujos divisores 
quadrados são um quadrado e depois a soma dos divisores quadrados.

Exemplo:
list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
A forma dos exemplos pode mudar de acordo com o idioma, veja “Testes de Amostra”.

Observação
Em Fortran - como em qualquer outra linguagem - a string retornada não pode conter 
nenhum espaço em branco redundante: você pode usar strings de caracteres alocadas dinamicamente.

'''

import math

def list_squared(m, n):
    def sum_of_divisors_squared(num):
        divisors_sum = 0
        # Itera por todos os números de 1 até a raiz quadrada de num
        for i in range(1, int(math.sqrt(num)) + 1):
            # Verifica se i é um divisor de num
            if num % i == 0:
                # Soma o quadrado de i aos divisores
                divisors_sum += i**2
                # Se i não for igual ao quociente da divisão (outro divisor), soma o quadrado dele também
                if i != num // i:
                    divisors_sum += (num // i)**2
        return divisors_sum

    result = []
    # Itera por todos os números no intervalo de m a n
    for num in range(m, n + 1):
        divisors_sum = sum_of_divisors_squared(num)
        # Verifica se a soma dos quadrados dos divisores é um quadrado perfeito
        if math.isqrt(divisors_sum)**2 == divisors_sum:
            # Se for um quadrado perfeito, adiciona o número e a soma à lista de resultados
            result.append([num, divisors_sum])
    return result

# Exemplos de uso:
print(list_squared(1, 250))
print(list_squared(42, 250))
