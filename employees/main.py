# created list object with 10 names
employees = [
    "Albin Zebi",
    "Roger Clemens",
    "Honus Wagner",
    "Stan Musial",
    "Ty Cobb",
    "Walter Johnson",
    "Hank Aaron",
    "Ted Williams",
    "Barry Bonds",
    "Willie Mays",
]

print("List of 10 employees name:\n", employees)

# putting the first 5 elements of the employees list
# to the new list subList1 using the slice operator
subList1 = employees[:5]
print("The first 5 employees:\n", subList1)

# putting the last 5 elements of the employees list
# to the new list subList2 using the slice operator
subList2 = employees[5:]
print("The last 5 employees:\n", subList2)

# appending the new employee to the subList2 using the append method
subList2.append("Kriti Brown")
print("The updated subList2 with the new employee added:\n", subList2)

# deleting the second element of the subList1 using the del operator
del subList1[1]
print("The updated subList1 with the second employee deleted:\n", subList1)

# creating a blank list named employees_new
employees_new = []

# adding the elements of the subList1 to the employees_new list
employees_new.extend(subList1)

# adding the elements of the subList2 to the employees_new list
employees_new.extend(subList2)
print("The new merged list:\n", employees_new)

# created list object with 10 salaries
salaryList = [100000, 80000, 70000, 70000, 90000, 80000, 60000, 70000, 80000, 70000]
print("The salary list:\n", salaryList)


# function that gives a rise of 4% to every employee
# and updates the salaryList
def give_rise(s):
    n = 0
    for e in s:
        s[n] = s[n] * 1.04
        n = n + 1
    print("The new salary list after a rise:\n", s)


give_rise(salaryList)

# sorted the salary list with the sort() method,
# used the parameter reverse=True to sort from the highest salary
# and used the slice operator to display only the first 3 elements
salaryList.sort(reverse=True)
print("The top 3 salaries after the rise:\n", salaryList[:3])
