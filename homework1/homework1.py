# File: homework1.py

# --------- Variables and Data Types -----------
print('# -----------------------------------------------------------------------------')
print('# SECTION 3.1')
print('# -----------------------------------------------------------------------------')

a = 10
print(a)
print(type(a))
# Is a whole number or a number without a decimal


b = 1.5
print(b)
print(type(b))
# A floating-point number representing a decimal value.


c = 3j
print(c)
print(type(c))
# A complex number where 'j' represents the imaginary number.


d = "hello"
print(d)
print(type(d))
# Text as a sequence of characters.


e = [1,2,3]
print(e)
print(type(e))
# An ordered, changeable collection of whole numbers.


f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))
# A mapping of unique keys to specific values.


g = (1,2)
print(g)
print(type(g))
# An ordered, unchangeable (immutable) sequence.

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))
# A list containing text elements.


i = True
print(i)
print(type(i))
# A logical type that can only be True or False.


j = None
print(j)
print(type(j))
# A special type representing the absence of a value.


k = [True, "blue", 12]
print(k)
print(type(k))
# A list containing multiple different data types.


l = str(14)
print(l)
print(type(l))
# An integer cast into a string or turning a number into text.


m = 1e4
print(m)
print(type(m))
# 10,000.0; scientific notation is a floating point

# Questions 3.1

# 1. There are 9 different data types

# 2. integer, float, complex, string, list, dictionary, tuple, boolean, NoneType

# 3. lists: e, h and k, strings: l and d , float: b and m

# 4.The data type for l was an integer. The str() method is a typer converter and converts it's parameter to a string

# 5. Another data type is set, the syntax is s = {}. It is not a dictionary. Disctionares use keys and vlues, seperated by a semicolon.
     # created set variables and assigned integer elements. passing the set variable to the str() converts it to a string.
     # The Following is an example of set values converted to string


print("\nQuestion 5 example\n")
set = {3,5,7,9}

print(f"Initial type: {type(set)} || Now the values are string {type(str(set))}\n")
 


print('# -----------------------------------------------------------------------------')
print('# SECTION 3.2')
print('# -----------------------------------------------------------------------------')

print(10 > 9)             # True  | since 10 is greater than 9.

print(10 == 9)            # False | since  10 is not equal to 9.

print(10 <= 9)            # False | 10 is neither less than nor equal to 9.

print(bool("abc"))                # True  | The string is not empty.

print(bool(123))                  # True  | The number is not zero.

print(bool(["apple", "cherry"]))  # True  | The list contains items.

print(bool(True))                 # True  | The value is explicitly True.

print(bool(False))                # False | The value is explicitly False.

print(bool(0))                    # False | The number zero is False

print(bool(""))                   # False | An empty string is False.

print(bool(" "))                  # True  | A string with a space is not empty

print(bool(()))                   # False | An empty tuple is False.

print(bool([]))                   # False | An empty list is False.

print(bool({}))                   # False | An empty dictionary is False.

print(bool(True and False))       # False | 'and' requires both sides to be True.

print(bool(True and True))        # True  | Both sides are True.

print(bool(False and False))      # False | Neither side is True.

print(bool(not(False)))           # True  | The opposite of False is True.

print(bool(not(True)))            # False | The opposite of True is False.

# Questions 3.2

# 1.
"""
TRUE : Values that are non zero. Any string with atleast one character. List, tuples, dictionary that has atleast one element inside.
       Comparison that accurately describes relistic qunatitative reasoning (5 > 4)

False: The number zero. Empty string. Empty list, tuple and dictionary.        

Logical: And only returns True if both expression on either side of and are True. Or returns True if either expressions of or are True or both are True as well.    
         not command switched the parameter from True to False and vice versa.
 

"""

# 2. 
"""
The results of the expressions did not surprise me. However, the bool expression with the logical and command 
with the False on the sides does seem strange at first glance but it does make sense. 
"""

#3.

print("\nQuestion 3 Exmaple\n")
print(bool(5 + 5 == 10 and 10 != 20))
"""
This gives True because both expressions are logically True

"""

#4. 

print("\nQuestion 4 Example\n")
print(bool(5 + 5 == 10 and 10 == 20))

"""
The expression is similar to the above, however it is False because 
one of the terms in the expression connected by the and logic is False, 
and therefore the entire expressions is False. 

"""

print('# -----------------------------------------------------------------------------')
print('# SECTION 3.3')
print('# -----------------------------------------------------------------------------')

# Arithmetic Operations
print("--- Arithmetic Operations ---")
print(f"10 + 5 = {10 + 5}")
print(f"10 - 5 = {10 - 5}")
print(f"2 * 4 = {2 * 4}")
print(f"6 / 3 = {6 / 3}")
print(f"5 % 2 = {5 % 2}")
print(f"3 ** 2 = {3 ** 2}")
print(f"15 // 2 = {15 // 2}")

# Comparison Operations
print("\n--- Comparison Operations ---")
print(f"5 == 2: {5 == 2}")
print(f"10 != 10: {10 != 10}")
print(f"2 < 5: {2 < 5}")
print(f"12 > 5: {12 > 5}")
print(f"5 <= 6: {5 <= 6}")
print(f"1 >= 10: {1 >= 10}")

# Assignment Operations
print("\n--- Assignment Operations ---")
x = 5
print(f"Initial x = {x}")
x += 5
print(f"x += 5 results in x = {x}")
x -= 4
print(f"x -= 4 results in x = {x}")
x *= 3
print(f"x *= 3 results in x = {x}")


# Logical Operators Questions



# 1. THE 'and' OPERATOR
"""The 'and' operator returns True only if BOTH statements on either side of it are True. 
If even one side is False, the entire expression becomes False."""

print("\nQuestion 1 Exmaple\n")

print(10 > 5 and 2 < 4)   # Both are True  -> Result: True

print(10 > 5 and 2 > 4)   # One is False   -> Result: False

print("\nQuestion 2 Exmaple\n")

"""The 'or' operator returns True if AT LEAST ONE of the statements is True. 
It only returns False if both statements are False."""

print(10 > 5 or 2 > 4)    # One is True, which is enough -> Result: True

print(10 < 5 or 2 > 4)    # Both are False -> Result: False

print("\nQuestion 3 Exmaple\n")

""" The 'not' operator is used to reverse the logical state of its operand. 
It turns True into False, and False into True. """

print(not(10 < 5))        # 10 < 5 is False, so not(False) -> Result: True

print(not(10 > 5))        # 10 > 5 is True, so not(True) -> Result: False


# More Questions

# 1. 

"""
The difference is the output of the results division. 
(/) Returns a decimal number (float), even if the result is a whole number.

(//) Returns the non decimal part of the number, and also rounds down to the
nearest whole number.


"""

# 2.
"""
The (//) returns the amount of times a number fits into another another ex. 7/2 = 3, the remainder is left out

The (%) returns the remainder amount ex. 7%2 = 1

""" 
# 3.
"""
The operator that would be used to return a remainder is the modulus operator or percent sign (%)

As explained in Q2

""" 

# 4.
"""
Assignments operators are used to store or update values in a variable

""" 


print('# -----------------------------------------------------------------------------')
print('# SECTION 3.4')
print('# -----------------------------------------------------------------------------')




print("\n--- Mutations of String ---\n")
my_string = "hello"

# 1. 
print(my_string) # Prints: hello (The full string value)

# 2. 
print(my_string[0]) # Prints: h (The first character at index 0)

# 3. 
print(my_string[1]) # Prints: e (The second character at index 1)

# 4. 
print(my_string[2]) # Prints: l (The third character at index 2)

# 5. 
print(my_string[3]) # Prints: l (The fourth character at index 3)

# 6. 
print(my_string[4]) # Prints: o (The fifth/last character at index 4)

# 7. 
print(my_string[-1]) # Prints: o (Negative indexing starts from the end; -1 is the last char)

# 8.
print(my_string[1:3]) # Prints: el (Slicing: starts at index 1, ends BEFORE index 3)

# 9. 
print(my_string[0:5:2]) # Prints: hlo (Slicing with a step: start at 0, end at 5, skip every 2nd char)

# 10. 
print(len(my_string)) # Prints: 5 (Total count of characters in the string)

# 11. P
print(my_string + "goodbye") # Prints: hellogoodbye (joining two strings together)

# 12. 
print(7 * my_string + "\n") # Prints: hellohellohellohellohellohellohello (String repetition)

# Questions

# 1.
"""

Slicing is the method used to extract specific sections of a sequence---like a string or a list.

"""

# 2.

print("Question 2\n")
name = "Oski"
print("Hello, my name is", name)

"""
The function print prints out the a string of characters, including spaces, and the variable name, 
that is seperated by a comma.

"""

# 3.

print("Question 3\n")
name = "Oski"
print(f"Hello, my name is {name}\n")

"""
The f before the curls tells the Python interpreter to look for 
curly braces and replace them with the value of the variable inside. 

"""

# 4.
"""
The difference between print and adding the f-string format inside print is the formatting.
In print alone, the print method is handling different objects at ones, where the f-string inclusing
builds one single string before printing. 
Also, print adds a space between arguments, while the f-string gives full control over spacing.

"""
print('# -----------------------------------------------------------------------------')
print('# SECTION 3.5')
print('# -----------------------------------------------------------------------------')

# 1. cd
# Definition: Moves you from your current folder into a different folder.
# How to use: Type 'cd' followed by the name of the folder you want to enter.
# Example: cd Documents

# 2. ls
# Definition: Lists the files and folders inside your current directory.
# How to use: Simply type 'ls'.
# Example: ls

# 3. ls -a
# Definition: Lists everything in the directory, including "hidden" files.
# How to use: Type 'ls' followed by the '-a' flag.
# Example: ls -a

# 4. mkdir
# Definition: Creates a new, empty folder.
# How to use: Type 'mkdir' followed by the name for the new folder.
# Example: mkdir python_projects

# 5. cat
# Definition: Displays the actual text content of a file directly in the terminal.
# How to use: Type 'cat' followed by the filename.
# Example: cat hello_world.py

# 6. pwd
# Definition: Tells you the full folder path of where you are currently located.
# How to use: Simply type 'pwd'.
# Example: pwd

# 7. cd ..
# Definition: Moves you "up" one level to the parent folder.
# How to use: Type 'cd' followed by two dots.
# Example: cd ..

# 8. cd .
# Definition: Refers to the directory you are currently in.
# How to use: Usually used to tell a program to look in the "current" spot.
# Example: python3 ./myscript.py

# 9. cd ~
# Definition: Instantly returns you to your user's main "Home" folder.
# How to use: Type 'cd' followed by the tilde symbol.
# Example: cd ~

# 10. cp
# Definition: Copies a file or folder from one location to another.
# How to use: Type 'cp', the source file, and the destination name.
# Example: cp notes.txt notes_backup.txt

# 11. mv
# Definition: Moves a file to a new folder OR renames a file.
# How to use: Type 'mv', the old name, and the new name.
# Example: mv old_name.txt new_name.txt

# 12. rm
# Definition: Deletes a file permanently. WARNING: No recovery!
# How to use: Type 'rm' followed by the filename.
# Example: rm unwanted_file.txt

# 13. clear
# Definition: Wipes the terminal screen clean of all previous text.
# How to use: Simply type 'clear'.
# Example: clear

# 14. grep
# Definition: Searches for a specific word or pattern inside a file.
# How to use: Type 'grep', the "word", and the filename.
# Example: grep "apple" fruits.txt

# Questions

# 1. Three additional Commands

# touch 
# Definition: Creates a new empty file
# How to use: touch followed by the filename
# Example: touch notes.txt

# whoami
# Definition: Displayes the username of the current user
# How to use: Type whoami
# Example: whoami 

# history
# Definition: Shows a list of all commands that have been typed recently
# How to use: Type history
# Example: history

# 2. Difference between ls and ls -a

"""
ls: 
It shows the files and folder(s) that are 'visible'. It skips over configuration
or system files.

ls -a:
the -a flags the command to show everything in the folder. The files mentioned above
including the hidden files

"""

# 3. What is a hidden file ? 

"""
A hidden file is any folder that starts with a period. They are usually 
configuration files. They are hidden in order for users to avoid deleting them.
Deleting them can unknowingly break something in the system.

"""

# 4. Three other Flags

#1.
# mkdir - p
# Define: It creates multiple folder down a path
# Example: mkdir -p python/projects/scrips

#2.
# mkdir -v
# Define: It prints the folders name that was created
# Example: mkdir -v new_folder_name

#3.
# rm -rf
# Define: Forces to delete files or folders (directory), ignoring all warning, deletes right away.
#rm -rf folder_name 

