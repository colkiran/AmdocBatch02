
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'd'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'Messi'), ('age', 35), ('goals', 350), ('club', 'PSG')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name='Ronaldo', age=37, goals=380, club='Al-Nasar FC')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
player = {'name': "lionel messi", 'age': 35, 'goals': 350, 'club': 'PSG'}
print(f"player :{player}")

print("-" * 40)
print(f"Name :{player['name']}")
print(f"Club :{player['club']}")

# iterate through the dictionary
print("-" * 40)
for x in player:
    print(x, "=>", player[x])       # will print all keys of the dictionary
print()

# modify dictionary
player['name'] = 'Messi'
player['country'] = 'Argentina'
player['goals'] = 365

print(f"player :{player}")

# delete
print("-" * 40)
del player['club']
del player['age']

print(f"player :{player}")

# print("-" * 40)
# print(dir(player))

print("keys".center(40, "-"))
player = {'name': 'Messi', 'age': 35, 'goals': 365, 'club': 'PSG', 'country': 'Argentina'}
print(f"player :{player}")

print("-" * 40)
k = player.keys()
print(k)

print("-" * 40)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(40, "-"))
player = {'name': 'Messi', 'age': 35, 'goals': 365, 'club': 'PSG', 'country': 'Argentina'}
print(f"player :{player}")

v = player.values()
print(v)
