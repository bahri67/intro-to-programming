# Exercise 3: Stripping Names :ballot_box_with_check:

#Tidy up the code to make it easier to understand

#Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

#Print the name once, so the whitespace around the name is displayed. 

#Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

# Define a name with extra whitespace around it, using \t for tab and \n for newline


name = "\t\n MOHD BAHRI \n\t"

print("Original name with whitespace:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip()) 
 