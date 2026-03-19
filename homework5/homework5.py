# Homework5.py






print('# -----------------------------------------------------------------------------')
print('# Homework 1 + 2 Review ')
print('# -----------------------------------------------------------------------------')

print('3.1')

# 1. Git vs. GitHub
# Git is the local software that tracks changes; GitHub is the cloud-based platform that hosts those tracked changes.

# 2. Terminal vs. Command Line
# Command Line is the interface where you type commands; the Terminal is the actual environment that runs that interface.


# 3. Local vs. Remote Repository
# Local: The project files stored on a local computer; Remote: The project files stored on a server (like GitHub).

# 4. Version Control
# A system that records changes to files over time so you can recall specific versions or undo mistakes later.

# 5. Staging Area
# An intermediate stage where you prepare specific changes before they are permanently saved to history.

# 6. git add
# Moves changes from the working directory to the Staging Area

# 7. git commit
# Permanently saves the staged changes into the local repository's history with a descriptive message.

# 8. git push
# Sends local commits to the remote repository in GitHub.

# 9. git status
# Shows the current state of the project: which files are modified, which are staged, and which are untracked.

# 10. git pull
# Fetches changes from the remote repository (GitHub) and merges them into your local project to keep it up to date.

# 11. pwd
# Displays the full path of the folder the user is currently in

# 12. ls 
# Lists all the files and folders inside your current directory.

# 13. cd 
# Moves you from your current folder into a different one 

# 14. nano
# A text-based editor inside the terminal used for writing or editing files quickly.

# 15. touch
# Creates a new, empty file with the name and extension specified

# 16. mv
# Used to either move a file to a different folder or rename a file.

# 17. rm
# Deletes a file permanently

# 18. cat 
# Displays the entire content of a file directly in the terminal window.

print('3.2')

# The command that will show the current working directory is pwd

# The command that will list all the files in the current directory is ls

# if you are in judy_decal, than going back cd ../brianna_repo && git pull will pull any updates from the repository'

# To move the homework (while in brianna's folder) to the homework folder copy homework.py ../judy_decal/homework.py

# To see the contents in termina, use the cat command, shows all code and comments

# The commands to push the file into the remote repository are git add . and then git commit -m 'Your descriptive message here' git push

"""

-The error means that the current version is behind the version that is in the remote repo. 
 Git requires that most recent history before it allows to add anything new to the file. 

- To resolve this, bring the recent changes to the loca repo, combine them with the material that has been added recently
  and then push again.

   The commands to update with changes that are remote, git pull origin main and then git push origin main to upload to remote

"""

# to go to recent from root, the absolute path while in terminal is cd /recent... since it is just right under.

print('3.3: directory drawing in homework5 folder')



print('# -----------------------------------------------------------------------------')
print('# Homework 3 Review')
print('# -----------------------------------------------------------------------------')


print('4.1')
def checkDataType(input_data):
     
     # Returns the name of the data type as a string 
    
    return type(input_data).__name__

print(checkDataType(3.14))   

print(checkDataType(True))   

print(checkDataType("Hi"))   

print(checkDataType([1, 2])) 

print("4.2")

def evenOrOdd(n):
    
    # Returns even if n is even, or odd otherwise 
    
    if n % 2 == 0:
    
        return 'Even'
    
    else:
    
        return 'Odd'


print(evenOrOdd(7))   

print(evenOrOdd(10))  


print('5')

def sum_(numbers):
    # Calculates the sum of a list using a for loop.
    
    total = 0  # Initialize the accumulator
    
    for num in numbers:
    
        total += num  # Add the current number to the running total
    
    return total


numbers_list = [1, 2, 3, 4, 5]

print(sum_(numbers_list))  

print('# -----------------------------------------------------------------------------')
print('# Homework 4')
print('# -----------------------------------------------------------------------------')


print('6.1')


def duplicateList(input):
    # Returns a new list where each element from the original appears twice.
    doubled_list = []
    
    for item in input:
        
        # Append the item twice for every one time it appears in the original
        
        doubled_list.append(item)
        
        doubled_list.append(item)
    
    return doubled_list


my_list = ['a', 'b', 'c']

print(duplicateList(my_list))  


print('6.2')

def square(num):
    return num * num

print(square(3))

# Colon was missing after paranthesis for parameter(s)

print('# -----------------------------------------------------------------------------')
print('# Favorite sunction')
print('# -----------------------------------------------------------------------------')

print(f'Squaring input:{square(4)}')

