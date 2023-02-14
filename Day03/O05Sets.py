
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print('-' * 40)
s2 = {1, 2, 3, 4, 'five', 6.5, 'seven', 'eight', 'nine', 10.3, 11.8, 12+4j, 12-4j, True, False}
print(f"s2 :{s2}")
print(type(s2))

print('-' * 40)
s3 = set(range(1, 11))
print(f's3 :{s3}')
print(type(s3))

print('-' * 40)
s1 = {1, 2, 3}
print(f"s1 :{s1}")

# add values into a set =>  add, update
# add
print('-' * 40)
s1.add(1)
s1.add(3)
s1.add(4)
s1.add(2)
s1.add(5)
s1.add(6)

print(f"s1 :{s1}")

# update
print('-' * 40)
s1.update([1, 2, 3])
s1.update([3, 4, 5])
s1.update([5, 6, 7])
s1.update([4, 5, 6])
s1.update([8, 9, 10])

print(f"s1 :{s1}")

# delete values from the set - pop, remove, discard

print('-' * 40)
print(f"s1 :{s1}")

res = s1.pop()
print(f"res :{res}")

res = s1.pop()
print(f"res :{res}")

print(f"s1 :{s1}")

print('-' * 40)
# remove

s1.remove(8)
s1.remove(4)
# s1.remove(1)
print(f"s1 :{s1}")

print('-' * 40)
# discard
s1.discard(6)
s1.discard(10)
s1.discard(1)

print(f"s1 :{s1}")

print('-' * 40)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print('-' * 40)
print(f"A union B :{A | B}")
print(f"B union A :{B.union(A)}")

print('-' * 40)
print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print('-' * 40)
print(f"A difference B :{A - B}")
print(f"B difference A :{B - A}")

print('-' * 40)
print(f"A symmetric difference B :{A ^ B}")
print(f"B symmetric difference A :{B.symmetric_difference(A)}")

print('-' * 40)
# frozen set are immutable
x = frozenset([1, 2, 3, 4, 5])
print(f"x :{x}")
print(type(x))
