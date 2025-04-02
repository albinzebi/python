# imports the module ast
import ast

# try statement to catch an exception
# opens and reads the data from the file dictionary.txt
try:
    with open("dictionary_reversed.txt") as f:
        data_in = f.read()
except FileNotFoundError:
    print("The file with the current name is not in this directory.")
except PermissionError:
    print("You can't access this file.")

# converts string data to dictionary
# and assigns it to variable d_og (dictionary original)
d_og = ast.literal_eval(data_in)


# creates a function that inverts a dictionary
def inverted_dictionary(d):
    inverse = dict()
    for key in d:
        value = d[key]
        if isinstance(value, list):
            for element in value:
                if element not in inverse:
                    inverse[element] = [key]
                else:
                    inverse[element].append(key)
        else:
            if value not in inverse:
                inverse[value] = [key]
            else:
                inverse[value].append(key)
    # replaces single-element lists with their only element
    for k, v in inverse.items():
        if len(v) == 1:
            inverse[k] = v[0]
    return inverse


# calls function with argument d_og
# and assigns the dictionary to variable d_new
d_new = inverted_dictionary(d_og)

# opens/creates the file dictionary_reversed.txt
# and writes inside the inverted dictionary
with open("dictionary_3.txt", "w") as data_out:
    data_out.write(str(d_new))
