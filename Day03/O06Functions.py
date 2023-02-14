
def greet():
    print("Greetings Mr. Messi, Welcome to the event.......")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.......")

# gname is non default argument, city is default argument
# non default arg cannot follow a default arg
def greetGstCty(gname,  city = "Barcelona"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event...........")

greet()

print("-" * 40)
greetGst("Messi")
greetGst("Ronaldo")

print("-" * 40)
greetGstCty("Messi")
greetGstCty("Neymar")
greetGstCty("Ronaldo", "Turin")

print("-" * 40)
# variable length arguments

def prodAll(*numbers):     # *numbers can accept more than one value and store it in a tuple
    print(f"numbers :{numbers}")
    prod = 1
    for number in numbers:
        prod *= number
    return prod

print(prodAll(1, 2, 3, 4, 5))

print("-" * 40)
def extractDetails(**details):
    print(details)
    print("-" * 40)
    for k, v in details.items():
        print(k, "=>", v)

extractDetails(name="Messi", age=35, goal=350, club='PSG', ballondor=7)

print("-" * 40)
def mulMe(x,  y):
    return x * y

print(f"The product of 5, 8 is :{mulMe(5, 8)}")

# using recursive calls find  - 1. factorial of a number, 2. Fibanoccoi series

print("-" * 40)
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

num = 5
print(f"The fact of num is :{fact(num)}")

print("-" * 40)
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

iter = 8
for i in range(iter):
    print(fibo(i), end=" ")
print()

print("-" * 40)
def arithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithCalc(20, 5)
print(res)

