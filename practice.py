# Christmas Tree
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


# Print out duplicates in a list
my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
unique = []
duplicates = []
for item in my_list:
    if item in unique:
        duplicates.append(item)
    else:
        unique.append(item)
print(duplicates)
print(' ')
# Same - Using comprehensions
comp_duplicates = list(set([item for item in my_list if my_list.count(item) > 1]))
print(comp_duplicates)
# New lines before next excercise
print(' ')
print(' ')


# Print hihest even number
def highest_even(lists):
    highest_even_number = 0
    for number in lists:
        if number % 2 == 0 and number >= highest_even_number:
            highest_even_number = number
    return highest_even_number
print(highest_even([10, 2, 3, 4, 8, 28, 11]))
# New lines before next excercise
print(' ')
print(' ')
