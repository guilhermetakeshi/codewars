numbers = [1, 0, 1, 1]

def binary_array_to_number(numbers):
    numeral = 0
    tam = len(numbers)
    
    while tam > 0:
        resto = numbers[tam-1]
        numeral = numeral + (resto * (2 ** (len(numbers) - tam)))
        tam -= 1
        
    return numeral

print(binary_array_to_number(numbers))


'''
Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11
'''

