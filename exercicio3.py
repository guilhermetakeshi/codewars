'''você escreverá uma função que retorna as posições e os valores 
dos “picos” (ou máximos locais) de um array numérico.

Por exemplo, a matriz arr = [0, 1, 2, 5, 1, 0] tem um pico na posição 3 com um 
valor de 5 (desde arr[3]igual a 5).

A saída será retornada como um objeto com duas propriedades: pos e picos. 
Ambas as propriedades devem ser matrizes. Se não houver pico na matriz fornecida, 
a saída deverá ser {pos: [], peaks: []}.

Exemplo: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])deveria retornar {pos: [3, 7], peaks: [6, 3]}

Todas as matrizes de entrada serão matrizes de números inteiros válidas (embora ainda possam estar vazias), 
portanto você não precisará validar a entrada.

O primeiro e o último elemento do array não serão considerados picos (no contexto de uma função matemática, 
não sabemos o que vem depois e antes e, portanto, não sabemos se é um pico ou não).

Além disso, cuidado com os platôs!!! [1, 2, 2, 2, 1]tem um pico enquanto [1, 2, 2, 2, 3]e [1, 2, 2, 2, 2]não. 
No caso de pico-platô, retorne apenas a posição e o valor do início do platô. Por exemplo: pickPeaks([1, 2, 2, 2, 1])
retornos {pos: [1], peaks: [2]}'''

def pick_peaks(arr):
    # Inicializa as listas vazias para armazenar as posições e os valores dos picos.
    pos = []
    peaks = []
    
    # Variável para rastrear o início de um platô.
    plateau_start = None
    
    # Percorre a lista a partir do segundo elemento (índice 1).
    for i in range(1, len(arr)):
        # Verifica se o elemento atual é maior do que o elemento anterior.
        if arr[i] > arr[i - 1]:
            # Se for maior, atualiza a variável plateau_start para marcar o início de um platô.
            plateau_start = i
        # Verifica se o elemento atual é menor do que o elemento anterior.
        elif arr[i] < arr[i - 1]:
            # Se for menor e houver um platô, adiciona a posição e o valor do platô às listas.
            if plateau_start is not None:
                pos.append(plateau_start)
                peaks.append(arr[plateau_start])
                plateau_start = None
    
    # Retorna um dicionário contendo as posições e os valores dos picos encontrados.
    return {"pos": pos, "peaks": peaks}

# Exemplo de uso:
arr = [3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]
resultado = pick_peaks(arr)
print(resultado)

