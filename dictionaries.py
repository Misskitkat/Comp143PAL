"""
This is just about dictionaries and how they work and how you can use them.
"""

meals = {'breakfast': 'bagel', 'lunch': 'sandwich', 'dinner': 'take-out'}
print(meals)
# this shows you the syntax of how it prints

print(meals['breakfast'])  # bagel
print(meals['lunch'])  # sandwich
print(meals['dinner'])  # take-out
# inside of dictionaries are key-value pairs.
# here, breakfast, lunch, and dinner are keys, and bagel, sandwich and take-out are values.
# you access the values by inputting the key, as you would input an index to get an element of a list.

meals['morning_snack'] = 'granola bar'
meals['afternoon_snack'] = 'cookies'
meals['evening_snack'] = 'ice cream'
# you can also add more key-value pairs to a dictionary.
print(meals)

# you can also start with an empty dictionary:
meals = {}
print(meals)
meals['breakfast'] = 'bagel'
meals['lunch'] = 'sandwich'
meals['dinner'] = 'take-out'
print(meals)

if meals['breakfast'] == 'eggs':
    print("that is a good breakfast")
elif meals['breakfast'] == 'bagel':
    print('thats an ok breakfast')
else:
    # assuming the option is worse than those two
    print('is that even a breakfast?')
# you can also use the dictionary in if statements like lists or variable comparisons

# say you dont eat breakfast:
del meals['breakfast']
print(meals)
# you can also remove items just like you did with lists.
# that dictionary value is gone and you cannot access it anymore.

meals = {'breakfast': 'bagel', 'lunch': 'sandwich', 'dinner': 'take-out'}

meals['snack'] = 'cookies', 'fruit', 'candy', 'nachos'
print(meals)
# you can also add multiple values to one key

print(meals['snack'])
# printing all of the values from that key
print(meals['snack'][0])
# you can access those the same type of way you do when you index into a list/tuple/etc

# another example with a for loop
favorite_lanuages = {
    'tom' : {'python', 'java'},
    'jessica' : {'c'},
    'cris' : {'rust', 'c++'},
    'louis' : {'java', 'c#', 'python'}
}

for name, languages in favorite_lanuages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for lanuage in languages:
        print(f"\t{lanuage.title()}")

# this way you can print the key name, and values, and the values separately and manipulate how they
# print to the terminal

