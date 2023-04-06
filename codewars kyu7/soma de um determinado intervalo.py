def get_sum(start, end):
    if start > end:
        numbers = range(end, start + 1)
    else:
        numbers = range(start, end + 1)
    #summ = lambda numbers: numbers+numbers , numbers
    summ = sum(numbers)
    
    return summ

print(get_sum(0, -1))

'''
melhor maneira: 

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
'''