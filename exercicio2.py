'''
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's 
divisors(except for 1 and the number itself), 
from smallest to largest. If the number is prime return the string
'(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

'''


def divisors(numero=13):
    numeros_divisiveis = []
    contador = 2
    while contador < numero:
        if numero % contador == 0:
            numeros_divisiveis.append(contador)
        contador+=1
    if len(numeros_divisiveis) == 0:
    	return "%s is prime" % (numero)
    else:
    	return numeros_divisiveis

print(divisors()) #should return [2,3,4,6]
#divisors(25) #should return [5]
#divisors(13) #should return "13 is prime"
