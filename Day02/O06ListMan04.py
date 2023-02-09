
print("copy".center(40, "-"))
l1 = list(range(1, 5))
print(f"l1 Before :{l1}")

l2 = l1             # shallow copy - copies the address along with data

print(f"l2 Before :{l2}")
l2.append(6)
l2.append(7)
l2.append(8)

print(f"l2 After :{l2}")
print(f"l1 After :{l1}")

print("=" * 40)
l3 = [10, 20, 30, 40, 50]
print(f"l3 Before :{l3}")

l4 = l3.copy()

print(f"l4 Before :{l4}")

l4.extend([60, 70, 80])
print(f"l4 After :{l4}")
print(f"l3 After :{l3}")

print("=" * 40)
l5 = [11, 22, 33, 44, [2, 4, 6, 8, 10], 55]
print(f"l5 Before:{l5}")

l6 = l5.copy()

print(f"l6 Before :{l6}")
l6[4].extend([12, 14, 16])

print(f"l6 After :{l6}")
print(f"l5 After :{l5}")

print("=" * 40)
l7 = [1, 2, 3, 4, [11, 22, 33, 44, 55], 5]
print(f"l7 Before :{l7}")

from copy import deepcopy
l8 = deepcopy(l7)

print(f"l8 Before: {l8}")
l8[4].extend([66, 77, 88])
print(f"l8 After :{l8}")
print(f"l7 After :{l7}")

