"""
this file is about how to use user input,
i will have a few inputs at the top so that they can be used anywhere else without needing to make more
variables for user input.
"""

noun = input("Enter a noun (can be person/place/thing [name works best]): ")
noun2 = input("Another noun (same options): ")
number = int(input("Enter an integer (string will throw an error): "))


print(f"Hello {noun.capitalize()} and {noun2.capitalize()}\n")

print(f"You are both {number} years old?\n")
# these show you how you can put the input into an fstring like a normal

if number >= 18:
    print("You could vote!! ")
else:
    print("You cannot vote child!")
# you can also use it in a comparison (as long as you have it as an int or use string comparison

i = 0
while i < number:
    print(i)
    i += 1
# you can also use it in a while loop as a way to loop through the length of the list

# maybe you want to find the sum of all the numbers in that number (like 1+2+3 = 6)?
sum = 0
i = 0
while i <= number:
    sum = sum+i
    i += 1
print(sum)


