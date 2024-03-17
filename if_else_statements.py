"""
Now where can you use those booleans that are in "boolean_logic"?
You can use them in if statements.
What are if and else statements?

If and else are ways to section off code depending on if a condition is correct.
For an example, if you have a pencil and paper, you can take notes,
if you do not have both, you will not be able to. That would be
an example of an if else statement
"""

# a simple example:
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# When you print this, you can see that only BMW is in all caps because when car is bmw if goes inside the
# first part of the if/else.
# When car isn't bmw, it goes inside the else part of the if/else.
# Both parts of the if/else will not both run, once one part of it runs, it exits the if/else.

# using the same car list as above
hated_car = "tesla"
if hated_car not in cars:
    print(f'{hated_car.title} cars are not available anyway!')

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
elif age <= 18:
    print("You are not able to vote yet.")
# elif is else if
# Did you predict this right? it should print the two statements in if and not touch the elif
# same type of comparison different age
age = 16
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
elif age <= 18:
    print("You are not able to vote yet.")

# what about more than 2?
age =  12
if age<4:
    print("abmission is free")
elif age < 18:
    print("admission is $25")
elif age <65:
    print("admission is $40")
else:
    print("admission is $25")
# you can see you can have an else but it is not required

# what can you do with lists?
requested_topping = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_topping:
    if requested_topping == 'green peppers':
        print("sorry ouf of green peppers")
    else:
        print(f'adding {requested_topping}.')
print('\n')
# what about an empty list
requested_topping = []
if requested_topping:
    for requested_topping in requested_topping:
        print(f"adding {requested_topping}")
else:
    print("Plain cheese pizza")

# what if you have multiple lists?

available_topping = ['olives', 'pineapple', 'sausage', 'mushrooms', 'extra cheese']
requested_topping = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_topping:
    if requested_topping in available_topping:
        print(f'adding {requested_topping}')
    else:
        print(f"{requested_topping} not available")
