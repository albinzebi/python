# creating Python dictionary
input_dictionary = {
    "Albin": ["CS1101", "CS1102", "ECON1580"],
    "Lucy": ["ECON1580", "CS1101", "CS1111"],
}

# printing the original dictionary
print("Here is the original dictionary:\n", input_dictionary)


# creating a function called inverted_dictionary
def inverted_dictionary(d):
    inverse = dict()
    for key, value in d.items():
        for element in value:
            if element not in inverse:
                inverse[element] = [key]
            else:
                inverse[element].append(key)
    return inverse


# printing the inverted dictionary
print("Here is the inverted dictionary:\n", inverted_dictionary(input_dictionary))
