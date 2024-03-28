"""
here is a short example to introduce for loops
"""

# add continue/break
# continue goes to top of loop and doesnt do code after
# break breaks it out of the entire loop

for i in range(0,10):
      if (i == 5):
            break
      else:
            print(f'{i} is not 5+')
            print("before continue")
            continue
            print("after continue")

