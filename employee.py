EMPNAME = ['Dom', 'Brian', 'Tej']
print("Initial list of employee names:", EMPNAME)

EMPNAME.append('Laty')
print("After appending 'Laty':", EMPNAME)

EMPNAME.remove('Brian')
print("After removing 'Brian':", EMPNAME)

EMPNAME.insert(1, 'Rom')
print("After inserting 'Rom' at index 1:", EMPNAME)

# Remove an element by index using pop()
removed_employee = EMPNAME.pop(2)
print("Removed", removed_employee, "from index 2:", EMPNAME)