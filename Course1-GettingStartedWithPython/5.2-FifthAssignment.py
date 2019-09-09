#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an 
# appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
# Maximum is 10
# Minimum is 2

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
         break
    try: 
        nval = int(num)
        if smallest is None and largest == None :
            smallest = nval
            largest = nval
        elif nval < smallest :
            smallest = nval
        elif nval > largest :
            largest = nval 
    except:
        print('Invalid input')
        continue


print("Maximum is", largest)
print("Minimum is", smallest)
