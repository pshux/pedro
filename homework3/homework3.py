# File: homework3.py
 
 
 
print('# -----------------------------------------------------------------------------')
print('# PRINT FUNCTIONS')
print('# -----------------------------------------------------------------------------')


def say_goodbye(name):
    return f"Good Bye, {name}"
 
print(say_goodbye("liz"))

def area_of_circle(r):
    
    # Calculates and returns area of a circle
    
    return 3.14 * r**2

print(f"Area of a circle {area_of_circle(2)}")

print('# -----------------------------------------------------------------------------')
print('# RETURN FUNCTIONS')
print('# -----------------------------------------------------------------------------')

def subtract(b, a):
    
    # returns a value after subtraction operation
    
    return b - a

print(f"After subtraction operation performed between a and b : {subtract(5,3)}")

def multiply(a, b):
    
    # returns value after multiplication operation between a and b
    
    return a * b


print(f"After multiplication operation performed on b and a: {multiply(5,3)}")

def divide(a, b):
    
    # returns value after division operation between a and b
    
    return a / b

print(f"After division operation performed on b and a: {divide(10,3):.2f}")

print('# -----------------------------------------------------------------------------')
print('# CONDITIONS')
print('# -----------------------------------------------------------------------------')

list = [15,14,17,20,23,28,20]

def max_min_temperatures(list):
    
    # returns max and min tuple by using min and max methods
    
    min_and_max = (min(list), max(list))
    
    
    return min_and_max

print(f"Returns min and max values as a tuple): {max_min_temperatures(list)}")
    

    
def is_weekend(number):
    
    # Takes input from user and returns True if weekend, False otherwise
    
    return True if number > 5 else False

print(f"Since the number is 6, then it is: {is_weekend(6)}")


def fuel_efficiency_calculator(m,g):
    
    # Takes in values for m for miles and g for gallons from user and returns m/g
    
    return m / g 

print(f"This the fueld efficiency of this vehicle: {fuel_efficiency_calculator(60,10)} m/g")

def secret_code(number):

   # Returns a shifted version 
   
   return (number % 10) * 10 ** (len(str(number)) - 1) +  number // 10


number = 12345
   
print(f"The number {number} is shuffled to : {secret_code(number)}")

print('# -----------------------------------------------------------------------------')
print('# LOOPS')
print('# -----------------------------------------------------------------------------')


def calculate_power(x, y):
    
    result = 1
    
    # loop to y times
    for _ in range(y):
    
        result *= x
    
    return result


print(f"x to the power of y is: {calculate_power(2, 3)}") 


def find_minimum(numbers):
    
    # initial value
    lowest = numbers[0]  
    
    # for loop goes through elements 
    # in order to compare
    
    for n in numbers:    
        
        # if current value in n is less than lowest, than assign and replace the initial value
        if n < lowest:   
    
            lowest = n   
    
    # after comparing, return the smallest value among elements
    return lowest


def find_maximum(numbers):
    
    # assign initial value
    highest = numbers[0]  
    
    # for loop goes through elements
    # in order to compare
    
    for n in numbers:     
        
        # if current vlaue in n greater than highest, then assign and replace the initial value
        if n > highest:  
    
            highest = n  
            
            # after comparisons, return highest value
    return highest



def find_min(numbers):
    
    # assigns initial value to min_val
    min_val = numbers[0]
    index = 1
    
    # while loops goes through list of numbers, checks if latter values are less than initial, if less assigns that value 
    while index < len(numbers):
       
        if numbers[index] < min_val:
       
            min_val = numbers[index]
       
        index += 1   # exits when reaches maximum index values (goes through all values)
        
    return min_val

def find_max(numbers):
    
    # assigns initial value to max_val
    max_val = numbers[0]
    
    index = 1
   
    # while loops goes through list of numbers, checks if latter values are more than initial, if less assigns that value 
    while index < len(numbers):
        
        if numbers[index] > max_val:
        
            max_val = numbers[index] # exits when reaches maximum index values (goes through all values)
        
        index += 1
        
    return max_val

def sum_digits_math(n):
    n = abs(n)
    total = 0
    
    # loops while n is greater than 0
    while n > 0:
       
        total += n % 10    # Adds the last digit to total
       
        n //= 10           # Remove the last digit in order to not add in total again
        
    return total

print(f"This is the sum of the digits: {sum_digits_math(212)}")  

print('# -----------------------------------------------------------------------------')
print('# FAVORITE FUNCTION')
print('# -----------------------------------------------------------------------------')
print(f"The function that has a nice algorithm is sum_digits methods: {sum_digits_math(323)}")