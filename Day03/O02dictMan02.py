
print("get".center(40, "-"))
player = {'name': 'Messi', 'age': 35, 'goals': 365, 'club': 'PSG'}
print(f"player :{player}")

print("-" * 40)
print("Name    :", player.get('name', "Invalid key, Please enter a valid one"))
print("Country :", player.get('country', "Invalid key, Please enter a valid one"))


print("fromkeys".center(40, "-"))
cities = ['blr', 'che', 'mum', 'del', 'kol', 'hyd', 'pun']
print(f"cities :{cities}")

res1 = dict.fromkeys(cities)
print(res1)

print("-" * 40)
res2 = dict.fromkeys(cities, 24)
print(res2)

print("setdefault".center(40, "-"))
player = {'name': 'Messi', 'age': 35, 'goals': 365, 'club': 'PSG'}
print(f"player :{player}")

player.setdefault('name', 'Lionel Messi')
player.setdefault('Club', 'FCB')
player.setdefault('country', 'Argentina')

print(f"player :{player}")

print("pop".center(40, "-"))
player = {'name': 'Messi', 'age': 35, 'goals': 365, 'club': 'PSG'}
print(f"player :{player}")

res = player.pop('age')
print(res)

res = player.pop('club')
print(res)

# res = player.pop()
# print(res)

print(f"player :{player}")

print("popitem".center(40, "-"))
player = {'name': 'Messi', 'age': 35, 'goals': 365, 'club': 'PSG'}
print(f"player :{player}")

res = player.popitem()
print(res)

res = player.popitem()
print(res)

print(f"player :{player}")

