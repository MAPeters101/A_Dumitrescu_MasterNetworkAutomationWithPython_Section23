
for number in range(10):
    print(number)
    if number == 5:
        break

#exit()
print('Outside for')

for letter in 'Python':
    if letter == 'o':
        print("Letter is 'o' and I'm breaking out of the loop ...")
        break
    print(letter)


for n in range(0, 20):
    if n% 13 == 0:
        print('There is a number divisible by 13 in the range. Breaking out...')
        break
else:
    print('There is a no number divisible by 13 in the range.')
print()

for n in range(1, 12):
    if n% 13 == 0:
        print('There is a number divisible by 13 in the range. Breaking out...')
        break
else:
    print('There is a no number divisible by 13 in the range.')
print()


for l in 'abc':
    print(l)
    for n in range(3):
        if n == 1:
            break
        print(n)