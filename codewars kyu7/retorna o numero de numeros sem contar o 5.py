def dont_give_me_five(start, end):
    # Cria uma sequência de números inteiros entre start e end, excluindo o end
    # Note que a função range() não inclui o último valor no intervalo, portanto end + 1 é utilizado
    numeros = range(start, end + 1)
    
    # Filtra a sequência de números, removendo o número 5
    numeros_sem_cinco = filter(lambda n: '5' not in str(n), numeros)
    
    # Retorna a quantidade de números na sequência sem o número 5
    return len(list(numeros_sem_cinco))

# Teste da função com os valores 4 e 17
print(dont_give_me_five(4, 17))  # Deve imprimir 12
