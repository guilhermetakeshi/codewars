'''
Quando você divide as potências sucessivas de 10 por 13, obtém os seguintes restos das divisões inteiras:

1, 10, 9, 12, 3, 4porque:

10 ^ 0 ->  1 (mod 13)
10 ^ 1 -> 10 (mod 13)
10 ^ 2 ->  9 (mod 13)
10 ^ 3 -> 12 (mod 13)
10 ^ 4 ->  3 (mod 13)
10 ^ 5 ->  4 (mod 13)
(Para "mod" você pode ver: https://en.wikipedia.org/wiki/Modulo_operation )

Então todo o padrão se repete. Daí o seguinte método:

Multiplicar

o dígito mais à direita do número com o número mais à esquerda na sequência mostrada acima,
o segundo dígito mais à direita com o segundo dígito mais à esquerda do número na sequência.
O ciclo continua e você soma todos esses produtos. Repita esse processo até que a sequência de somas fique estacionária .

Exemplo:
Qual é o resto quando 1234567é dividido por 13?

7      6     5      4     3     2     1  (digits of 1234567 from the right)
x      x     x      x     x     x     x  (multiplication)
1     10     9     12     3     4     1  (the repeating sequence)

Portanto seguindo o método obtemos:

7x1 + 6x10 + 5x9 + 4x12 + 3x3 + 2x4 + 1x1 = 178

Repetimos o processo com o número 178:

8x1 + 7x10 + 1x9 = 87

e novamente com 87:

7x1 + 8x10 = 87

De agora em diante a sequência é estacionária (sempre obtemos 87) e o resto de 1234567 by 13é igual ao resto de 87by 13(ou seja 9).

Tarefa:
Chame thirta função que processa esta sequência de operações em um número inteiro n (>=0). thirtretornará o número estacionário .

thirt(1234567)calcula 178, depois 87, depois 87 e retorna 87.

thirt(321)calcula 48, 48 e retorna 48
'''

# 1 - inverter a ordem dos numeros
# 2 - pegar separadamente cada numero
# 3 - multiplicar pela sequencia

def thirt(n):
    sequence = [1, 10, 9, 12, 3, 4, 1]
    n_str = str(n)
    n_str = n_str[::-1]
    multpli = []
    
    for i in range(len(n_str)):
        #mult = int(n_str[i]) * sequence[i]
        mult = int(n_str[i]) * sequence[i % len(sequence)]
        multpli.append(mult)
    
    result = sum(multpli)

    # Verifique se o resultado é igual ao valor original (n) como número inteiro
    if result == n:
        return result
    else:
        # Chame recursivamente a função e retorne o resultado da chamada recursiva
        return thirt(result)

n = 321
resultado = thirt(n)
print(resultado)