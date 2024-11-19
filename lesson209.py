
# while True:
#     guess = int(input('Enter your lucky number [1-10]: '))
#     if guess == 7:
#         print('You won!')
#         break
#     print(f'{guess} was not the lucky number.')


a = int(input('Enter number: '))
while a > 1:
    b = a // 2
    while b > 1:
        if a % b == 0:
            break
        b -= 1
    else:
        print(f'{a} is prime.')
    a -= 1