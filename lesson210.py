
print(x := 2 + 3)
print(f'x is {x}')

# print(y=10)
print()


# value = input('Enter something: ')
# while value != '':
#     print(f'You entered: {value}')
#     value = input('Enter something: ')

# while(value := input('Enter something: ')) != '':
#     print(f'You entered: {value}')

# data = input('Enter your name: ')
# if len(data) > 0:
#     print(f'Your name has {len(data)} characters.')
# else:
#     print('Your name can not be empty.')


data = input('Enter your name: ')
if (n := len(data)) > 0:
    print(f'Your name has {n} characters.')
else:
    print('Your name can not be empty.')