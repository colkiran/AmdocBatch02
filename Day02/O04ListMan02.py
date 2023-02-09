
# delete values from a list - pop, remove, clear

l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(6)
print(res)

res = l1.pop(1)
print(res)

res = l1.pop()
print(res)

# res = l1.pop(9)
# print(res)

print(f"l1 :{l1}")

print("remove".center(40, "-"))

l1 = [1, 2, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1]

print(f"l1 :{l1}")
l1.remove(3)
l1.remove(3)
l1.remove(3)
# l1.remove(3)

print(f"l1 :{l1}")

# while l1.count(1):
#     l1.remove(1)

# print(f"l1 :{l1}")

res = [x for x in l1 if x != 1]
print(f"res :{res}")

print("clear".center(40, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")

print('count'.center(40, "-"))
l1 = [1, 2, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1]

print(f"l1 :{l1}")

print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")

print('index'.center(40, "-"))
l1 = [1, 2, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1]

print(f"l1 :{l1}")

print("3 :", l1.index(3))
print("3 :", l1.index(3, l1.index(3) + 1))
print("3 :", l1.index(3, l1.index(3, l1.index(3) + 1)+1))

