
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.2, 8.5, 9.0, 10+0j, 11-0j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
# memory allocation
l4 = [1, 2, 3, 'four', 'five', 'six', 7.2, 8.5, 9.0, 10+0j, 11-0j, True, False]
print(f"l4 :{l4}")
print(id(l4[0]))
print(id(l4[1]))
print(id(l4[2]))
print(id(l4[3]))

print("-" * 40)
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")
l1[3] = 3.5
print(f"l1 :{l1}")

del l1[3]
print(f"l1 :{l1}")

# print("-" * 40)
# print(dir(l1))

# add new values into a list - append, extend, insert

print("append".center(40, "-"))
l1  = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")
print(type(l1))

l1.append(6)
l1.append(7)
l1.append(8)

print(f"l1 :{l1}")
l1.append([9, 10, 11, 12, 13, 14])
print(f"l1 :{l1}")

print(l1[8])
print(l1[8][2:5])

print("extend".center(40, "-"))
l2 = ['a', 'b', 'c', 'd', 'e']
print(f"l2 :{l2}")

l2.extend(['f', 'g', 'h', 'i', 'j'])
print(f"l2 :{l2}")

print("insert".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 3.5)

print(f"l1 :{l1}")

print(len(l1))

l1.insert(15, 100)
print(f"l1 :{l1}")

print(len(l1))

print("-" * 40)
import numpy as np
from sys import getsizeof

l1 = list(range(1, 1000))

arr = np.array(range(1, 1000))

print(getsizeof(l1))
print(getsizeof(arr))

