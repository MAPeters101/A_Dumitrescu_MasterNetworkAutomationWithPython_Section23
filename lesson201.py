
for letter in 'Python':
    print(letter)
    print('bye')
print('########')

for letter in [1, 2, 3]:
    print(letter)

for letter in (1, 2, 3):
    print(letter)

for letter in {1, 'a', 'b'}:
    print(letter)

# for letter in 8:
#     print(letter)

my_str = input('Enter something: ')
vowels = 'aeiou'
for item in my_str:
    if item in vowels:
        print(item, end=' ')


