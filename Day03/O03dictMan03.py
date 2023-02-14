
print("items".center(40, "-"))

emp = {
    'emp1': {'name': 'Mike', 'age': 34, 'dept': 'finance', 'desig': 'MGR', 'sal': 85000},
    'emp2': {'name': 'Mary', 'age': 30, 'dept': 'HR', 'desig': 'HR Executive', 'sal': 45000},
    'emp3': {'name': 'Steve', 'age': 32, 'dept': 'IT', 'desig': 'TL', 'sal': 75000}
}

print(f"emp :{emp}")
print("-" * 40)

print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("-" * 40)
# keys and values
for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k,v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("update".center(40, "-"))

emp1 = {'name': 'Mike', 'age': 34, 'dept': 'finance', 'desig': 'MGR'}
emp2 = {'name': 'Mary', 'age': 30, 'dept': 'HR', 'sal': 45000}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("-" * 40)
emp1.update(emp2)

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("clear".center(40, "-"))
emp1 = {'name': 'Mike', 'age': 34, 'dept': 'finance', 'desig': 'MGR'}
print(f"emp1 :{emp1}")

emp1.clear()
print(f"emp1 :{emp1}")

print("copy".center(40, "-"))
emp1 = {'name': 'Mike', 'age': 34, 'dept': 'finance', 'desig': 'MGR'}
print(f"emp1  Before :{emp1}")

emp2 = emp1             # shallow copy - copies the address along with the data

print(f"emp2 Before :{emp2}")

print("-" * 40)
emp2['sal'] = 45000
emp2['loc'] = 'Hyd'

print(f"emp2 After :{emp2}")
print(f"emp2 After :{emp2}")

print('\n', "-" * 40, '\n')
emp3 = {'name': 'Mary', 'age': 30, 'dept': 'HR', 'sal': 45000}
print(f"emp3 Before :{emp3}")

emp4 = emp3.copy()                  # deepcopy

print(f"emp4 Before :{emp4}")
emp4['desig'] = 'TL'
emp4['loc'] = 'Delhi'

print("-" * 40)
print(f"emp4 After :{emp4}")
print(f"emp3 After :{emp3}")

print('\n', "-" * 40, '\n')
emp5 = {'name': 'Mike', 'age': 34, 'dept': 'finance', 'desig': {'wipro': 'Trainee', 'ibm' : 'Accountant', 'hp':'Sr. Accountant'}, 'sal': 85000}
print(f"emp1 Before :{emp1}")

emp6 = emp5.copy()

print(f"emp6 Before :{emp6}")

emp6['desig']['tesco'] = 'TL'
emp6['desig']['sap'] = 'TM'

print("-" * 40)
print(f"emp6 After :{emp6}")
print(f"emp5 After :{emp5}")

print('\n', "-" * 40, '\n')
emp7 = {'name': 'Mike', 'age': 34, 'dept': 'finance', 'desig': {'wipro': 'Trainee', 'ibm' : 'Accountant', 'hp':'Sr. Accountant'}, 'sal': 85000}
print(f"emp7 Before: {emp7}")
from copy import deepcopy

emp8 = deepcopy(emp7)

print(f"emp8 Before :{emp8}")
emp8['desig']['tesco'] = 'TL'
emp8['desig']['sap'] = 'TM'

print("-" * 40)
print(f"emp8 After :{emp8}")
print(f"emp7 After :{emp7}")