numbers = [1, 2, 3, 4, 5]

def remove_smallest(numbers):
    bigger = min(numbers)
    smallest = max(numbers)

    for number in numbers:
        if number < smallest:
            smallest = number

    first_occurrence = numbers.index(smallest)
    numbers.pop(first_occurrence)

    return numbers

print(remove_smallest(numbers))

'''
----------------------------------------------------------
    
def remove_smallest(numbers):
    smallest = min(numbers)
    first_occurrence = numbers.index(smallest)
    numbers.pop(first_occurrence)

    return numbers
'''