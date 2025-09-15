# 1. Write a python program to display a user entered name followed by Good
name = input("Enter your name: ")

print(f"Good Afternoon, {name} ") 

# . Write a program to fill in a letter template given below with name and date.

letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"

print(letter)



# Replace the double space from problem 3 with single spaces.

name = "Harry is a good  boy and  "

print(name.replace("  ", " "))
print(name) # Strings are immutable which means that you cannot change them by running functions on them