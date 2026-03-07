# File Name: Homework 4

print('# -----------------------------------------------------------------------------')
print('# LISTS')
print('# -----------------------------------------------------------------------------')

print("3.1")

list = ["peanuts", "cashews",'pistachios', 'sesame seeds','rasberries']

print(f"1. The second food in the list is : {list[1]}")


print(f"2. The last food in the list is : {list[-1]}")

add_to_list = 'avocados'

print(f"3. Adding {add_to_list} to the list ")

list.append(add_to_list)

print(list)

print(f"4. Adding apple to the list ")

list.insert(0,'apple')

print(list)

print(f"5. Removing the third item in the list ")

del list[2]

print(list)

print(f"6. The length of the list is {len(list)}")

print(f"7.Looping through the loop and upper case the list {[new_food_list.upper() for new_food_list in list]}")

first_and_last = list[:1] + list[-1:]

print(f"8. New list containing first and last items in list {first_and_last}")

item = 'potato'

print(f"9. Looking for Potato in list: {'A potato' if item in list else 'Not found'}")

print('# -----------------------------------------------------------------------------')
print('# 3.2 SLICING AND STRIDING')
print('# -----------------------------------------------------------------------------')


del list

numbers = list(range(21))

def get_first_15(lst):
    """Returns the first 15 elements (indices 0 through 14)."""
    return lst[:15]

def get_every_5th(lst):
    """Returns every 5th element from the list."""
    return lst[::5]

def reverse_and_stride(lst):
    """Reverses the list and then returns every 3rd element."""

    reversed_lst = lst[::-1]

    return reversed_lst[::3]


step1 = get_first_15(numbers)

step2 = get_every_5th(step1)

step3 = reverse_and_stride(step2)


print(f"Step 1 (First 15): {step1}")

print(f"Step 2 (Every 5th): {step2}")

print(f"Step 3 (Reverse & Stride 3): {step3}") 

print('# -----------------------------------------------------------------------------')
print('# 3.3 NESTED')
print('# -----------------------------------------------------------------------------')


print('3.3.1')
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print(f"Third Row: {numbers[2]}") 


print(f"Second item, Second row: {numbers[1][1]}")

numbers.append([10, 11, 12])

print(f"Updated List: {numbers}")

def sum_nested(lst):
    total = 0
    
    for row in lst:
    
        for num in row:
    
            total += num
    
    return total

grand_total = sum_nested(numbers)

print(f"The total sum is: {grand_total}")

print('# -----------------------------------------------------------------------------')
print('# 3.4 CREATE A 5X5 LIST')
print('# -----------------------------------------------------------------------------')

def create_5x5():
    
    grid = []
    
    counter = 1
    
    for i in range(5):        # Create 5 rows
    
        row = []
    
        for j in range(5):    # Create 5 columns
    
            row.append(counter)
    
            counter += 1
    
        grid.append(row)
    
    return grid

numbers_grid = create_5x5()

def replace_multiples(grid):
    # create a copy or a new list to store the updated version
    
    updated_grid = []
    
    for row in grid:
    
        new_row = []
    
        for item in row:
    
            if item % 3 == 0:
    
                new_row.append("?")
    
            else:
    
                new_row.append(item)
    
        updated_grid.append(new_row)
    
    return updated_grid

modified_grid = replace_multiples(numbers_grid)


def sum_filtered(grid):
    total = 0
    
    for row in grid:
    
        for item in row:
    
            if item != "?":
    
                total += item
    
    return total

final_sum = sum_filtered(modified_grid)

print("Modified Grid:")

for r in modified_grid: print(r)

print(f"\nThe sum of all numbers (excluding '?') is: {final_sum}")

print('# -----------------------------------------------------------------------------')
print('# 4 Dictionaries')
print('# -----------------------------------------------------------------------------')

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}



print(f"Katie is {ages['Katie']} years old.")

ages["Mira"] = 100

ages["Milana"] = 52

del ages["Mariam"]

print(ages) 


for name, age in ages.items():
    print(f"{name} is {age} years old.")
    
print('# -----------------------------------------------------------------------------')
print('# 5.2 FAVORITE FUNCTION')
print('# -----------------------------------------------------------------------------')


print(f"\nThe sum of all numbers (excluding '?') is (recalled): {final_sum}")