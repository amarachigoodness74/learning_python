picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

fill = '*'
empty = ' '
for row in picture:
    for dot in row:
        if (dot):
            # end='' - Remove the new line added after every print
            print(fill, end='')
        else:
            print(empty, end='')
    print(' ')  # Add a new line after every row

# New lines before next excercise
print(' ')
print(' ')

my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
unique = []
duplicates = []

for item in my_list:
    if item in unique:
        duplicates.append(item)
    else:
        unique.append(item)
print(duplicates)

# New lines before next excercise
print(' ')
print(' ')


def highest_even(lists):
    highest_even_number = 0
    for number in lists:
        if number % 2 == 0 and number >= highest_even_number:
            highest_even_number = number
    return highest_even_number


print(highest_even([10, 2, 3, 4, 8, 28, 11]))
