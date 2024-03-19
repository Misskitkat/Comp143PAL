"""
This part of the project is to show how you can print strings,
and what you can do with strings,
the variable names do not have to be specifically what I did, they are just examples.

Feel free to comment lines out so that you can see what each line does on its own, be careful to not
comment variables you are actively using.
(Use the # symbol to comment)

Feel free to try some of these out on your own or use them as reference for future python or coding projects in
general.
"""

# this is one way to type out a hello world
print("hello world")
# this is another way to type out a hello world, showing that single and double quotes both work for a string
print('Hello world')

# this is showing how to print a variable
helloWorld = "hello world"
print(helloWorld)

# another few methods
hello_variable = "hello"
world_variable = "world"

print(hello_variable + world_variable)
print(hello_variable + " " + world_variable)
# what is different about this one and the one above it ^

# this one is an f string where it inputs the variable value into the {space}
print(f'{hello_variable} {world_variable}')

# this one acts like a few above it where you never add a space between them so the two words are together
fullString = hello_variable + world_variable
print(fullString)
#or
fullString = f'{hello_variable} {world_variable}'
print(fullString)

# these show you how you can change the case of the words printed
# title makes the first letter of the string capital
print(hello_variable.title())
# lower will not change it because it is already all lowercase
print(hello_variable.lower())
# upper makes the whole thing uppercase
print(hello_variable.upper())

# this one shows how it makes each first letter of each word a capital vs only the first letter
print(fullString.title())

# this will strip the first or last character depending on if you use strip, rstrip, lstrip (book page 22&23)
# and can change the inside to be something, but if you don't put anything there it strips empty spaces like ' '
print(hello_variable.strip('h'))

print("This can't run right without the double quotes outside.")
print('A quote: "(insert famous quote here)"')
# hopefully you see the difference between the top and bottom
# the double quotes are needed when the print statement requires a single quote and vice versa


string_to_print = "hello world "
print(string_to_print*3)

string_divider = "--"
print(string_divider*80)

print("(questions for quiz go here [example])")

print("\ta. answer 1")
print("b. \n answer 2")

print("Hello world\n"
      "\thello world\n")
