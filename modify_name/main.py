# initiate variable name with string 'Albin'
name = 'Albin'
print('Your name is', name)

# variable that asks the user to specify the number of characters
n = int(input('Starting from the left, how many characters to display: '))

# function that prints the short name
def n_characters_from_left(n):
    short_name = name[:n] # using bracket operator on variable name
    print('Here is the short name:', short_name)

# calls function
n_characters_from_left(n)

# function that counts the number of vowels
def count_vowels(name):
    vowels = 0
    for c in name:
        if c in 'aeiouAEIOU':
            vowels = vowels + 1
    print('There are', vowels, 'vowels in the name', name)

# calls function 
count_vowels(name)       

# function that reverses the string assigned to the variable name
def reversed_name(name):
    index = -1
    name_length = len(name)
    backwards_name = ''
    while index >= -name_length:
        letter = name[index]
        backwards_name = backwards_name + letter
        index = index - 1
    print('Your name in reverse is:', backwards_name)

# calls function
reversed_name(name)
