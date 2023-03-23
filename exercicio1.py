'''
Implement a function that accepts 3 integer values a, b, c. 
The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 
to be accepted).
'''

def is_triangle(a=1, b=2, c=2):
   if ((b - c) < a < (b + c)) or ((a - c) < b < (a + c)) or ((a - b) < c < (a + b)):
        return True
   else:
       return False
print(is_triangle())