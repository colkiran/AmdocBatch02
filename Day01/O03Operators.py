
print("Arithmetic Operators".center(40, '-'))
print(f"add : 5 + 3 = {5 + 3}")
print(f"sub : 5 - 3 = {5 - 3}")
print(f"mul : 5 * 3 = {5 * 3}")
print(f"div : 5 / 3 = {5 / 3}")         # float
print(f"floor : 5 // 3 = {5 // 3}")     # integer
print(f"mod : 5 % 3 = {5 % 3}")
print(f"exp : 5 ** 3 = {5 ** 3}")

print("Augmentor".center(40, "-"))
# =, +=, -=, *=, /=
x = 10
print(f"x :{x}")

x += 5
print(f"x :{x}")

x /= 5
print(f"x :{x}")

print("comparison".center(40, "-"))
# ==, >, >=, <, <=, !=
a = 10
b = 5
print(f"a == b :{a == b}")
print(f"a >= b :{a >= b}")
print(f"a <= b :{a <= b}")
print(f"a != b :{a != b}")

print("Logical".center(40, "-"))
# and, or, not
print(1 == 1 and 2 == 2)
print(1 == 1 and 2 == 1)

print(1 == 2 or 2 == 1)
print(1 == 2 or 2 == 2)

print(not(1 == 2 or 2 == 1))
print(not(1 == 2 or 2 == 2))

print("-" * 40)
print(f"ord('A') :{ord('A')}")      # integer representation of unicode character
print(f"ord('Z') :{ord('Z')}")
print(f"ord('a') :{ord('a')}")
print(f"ord('z') :{ord('z')}")

print("bitwise".center(40, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")

print(f"5 >> 1 :{5 >> 1}")

print("ternary".center(40, "-"))
a = 20
print("Eligible" if a >= 18 else "Not Eligible")
