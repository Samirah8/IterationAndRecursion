# Samirah Ali, Course: 261, Lab Title: IterationAndRecursion

def factorial_iterative( n ):
    factorial_iterative = 5
    result = 1
    for i in range(n) :
        result *= i + 1
    return result
 
for i in range (5):
   print ('Factorial results using an interative function')
   print ('0! =', factorial_iterative(0))
   print ('5! =', factorial_iterative(5))
   print ('10! =', factorial_iterative(10))
   print ('25! =', factorial_iterative(25))
   print ('50! =  ', factorial_iterative(50))
   print ('100! = ', factorial_iterative(100))




