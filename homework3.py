# File: homework3.py
 
 
 
print('# -----------------------------------------------------------------------------')
print('# PRINT FUNCTIONS')
print('# -----------------------------------------------------------------------------')

def say_goodbye(name):
     
     # returns name variable with string "Good Bye" added together
     
     return f"Good Bye,{name}"
 
 
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


print(f"After multiplication operation performed on b and a:{multiply(5,3)}")

def divide(a, b):
    
    # returns value after division operation between a and b
    
    return a / b

print(f"After division operation performed on b and a: {divide(10,3)}")

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
    
    # Takes in values for m for miles and g for gallons from user and returns m
    
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


def find_minimum(numbers):
    lowest = numbers[0]  # Start with the first number
    for n in numbers:    # Loop through every number
        if n < lowest:   # Comparison
            lowest = n   # Update if a smaller one is found
    return lowest


def find_maximum(numbers):
    
    highest = numbers[0]  # Assume the first is the biggest
    for n in numbers:     # Check every number
        if n > highest:   # If current number is greater than our record
            highest = n   # Update the record
            
    return highest