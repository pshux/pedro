# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?

"""
Git : Is as software that tracks changes in files. It is stored locally in the computer
      It is a version control. It works offline. 

Git Hub: Is a website that hosts git repositories. It is a cloud based hosting service. 
         It allows to upload (push) local git snapshots to share or work on in different devices.

Git Bash: Is an application for Windows users that provides "Bash" terminal enviorment to run git.
          It is a command line interface. This allows Windows computers to use the same commands as macOS or Linux.
          
"""

# 2) What’s the difference between the terminal and the command line?
"""
Terminal: Is the enviorment that lets you type. Basically a window that let's
          a user interact with the a system. 

Command Line: It is the space where you provide instructions, basically a line where
              a user puts instructions. 

"""

# 3) How does Windows PowerShell differ from Git Bash?
"""
Git Bash: Bash is the standard language for Linux and macOS that Git uses. Git Bash
          treats all input as text or a string of characters.

Power Shell: Is a language based on the .NET framework. While it recognizes some Bash commands
             its native commands are different. It treats inputs as objects; it sees data objects with properties
             (size, creation date, permissions).

"""


# 4) What’s the difference between Anaconda, conda, and Python?

"""
Python: Is the programming lanague. It sets the rules, and the interpreter that reads
        the code put together and makes things happen. 

conda: Is a package manager and enviorment manager. It is a command line program that installs libraries
       and manage enviorments.

Anaconda: It is a package that includes Python, the conda tool and over 1000 python libraries.

"""


# 5) What is VS Code? 

"""

VS Code: Is a code editor that has the capabilities to be cunstomised into an Integrated Development Enviorment. 

"""


# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?

"""
Jupyter Notebook: A web based interactive enviorment that combines, code, equations, visualizations a
                  nd narrative text (Markdown).
                  Cells are it's core feature. It's lets the user run code one cell at a time, 
                  nstead of a whole script.
                  The output appears under the cell. 

Jupyter Lab: It is a dashboard that allows the user to with multiple notebooks, text files, and terminals 
             all at once in a single browser.
             It allows multi-tasking. An example  is have a a Notebook open on one side while 
             having a terminal or CSV file open.
             It allows drag and drop cells across Notebooks.

"""

# 7) What does ~/ mean?

"""

~/: Is a short cut that represents the users Home Directory.

"""


# 8) What’s the difference between an absolute path and a relative path?

"""
Absolute Path: Is the method used to go to a directory starting from the root directory as a path.
               It is a full address path /users/oski/python/script.py

Relative Path: Describes the location of a file or folder relative to the current working directory.
               It is the action of moving step by step to different directories relative to the current directory.

"""

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".

"""

Absolute Path: cd /users/user_name/folder/python_decal_spr26/course_assignments

Relative Path  cd ../course_assignments       # Since the current directory is the repo

"""

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?

"""
cd .. : Change Directory with two dots let's the user jump to the previous directory in the path.
        In this case from homework2 back to course_assigments.
"""

# 11) What would rm ./ do in your current directory? (Don’t try it!)

"""

rm ./: It will try to delete everyhing in the current directory.

"""


# 12) What do the following commands do?

"""
git add: It moves the changes in a working directory to the staging area.


git commit: It takes everything in the staging area and created a snapshort or saving point
            in the local repository


git push: It uploads the local commit to a remote repository ie. GitHub


"""

# 13) What's the difference between "git add ." and "git add <file>"?
"""

git add . : This command moves all of the repo directories files and sub 
files that have been modified and moves it to the stage

git add <file> : This command only moves only the file desired to the stage.


"""

# 14) What do "git status" and "git log -1" do?

"""

git status: It shows the current state of the working directory and staging area
            or shows the files have been modified, not staged, and what branch you are in. 

git log -1: Command shows the history of all saves (commit) and descriptions written

"""

# 15) What’s the difference between cloning a repository and pulling from it?

"""

Cloning: It creates a folder with all the files that is being cloned and brings over the entire history
         of commits for those files. It connects the local folder to the remore file.

Pulling: It looks at the online repository, sees what is different between the version that is local and the 
         remote one and merges those changes in the local file. 

"""

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?

"""

It was connecting the local repository to remote using Git. 


"""

# 17) What’s a question you still have? What’s something you’re confused about?

"""

Is there data analysis ?

"""


# 18) Tell me a fun fact!

"""

Biology is complex


"""

# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)

# This expression or method takes the first numerical parameter and powers it to the second parameter

print(f"This expression or method prints out an exponential operation: {pow(5,3)}") 
