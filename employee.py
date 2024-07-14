EMPNAME = ['Dom', 'Brian', 'Tej']
print("Initial list of employee names:", EMPNAME)

EMPNAME.append('Laty')
print("After appending 'David':", EMPNAME)

EMPNAME.remove('Brian')
print("After removing 'Bob':", EMPNAME)

EMPNAME.insert(1, 'Rom')
print("After inserting 'Eve' at index 1:", EMPNAME)

# Remove an element by index using pop()
removed_employee = EMPNAME.pop(2)
print("Removed", removed_employee, "from index 2:", EMPNAME)