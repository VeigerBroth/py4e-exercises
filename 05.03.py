"""
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with a try/except and put out an 
appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
"""

smallest = None
maximum = 0

while True:
    enter = input('Enter number or done to end loop: ')
    
    try:
        enter = int(enter)
        if smallest is None:
            smallest = enter
        elif enter < smallest:
            smallest = enter
        elif enter > maximum:
            maximum = enter
    except:
        if enter != 'done':
            print('Invalid input')
            continue
    
    if enter == 'done': break
    
print('Maximum is ', maximum)
print('Minimum is ', smallest)
    
