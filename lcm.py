def lcm(x, y):
    greater_number = max(x, y)
    while(True):
        if((greater_number % x == 0) and (greater_number % y == 0)):
            lcm = greater_number
            break
        greater_number += 1
    return lcm

num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))

print(f'The L.C.M. of {num_1} and {num_2} is {str(lcm(num_1, num_2))}')