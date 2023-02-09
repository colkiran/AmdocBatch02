
"""
sort -   will sort the original list
sorted -  takes a copy of the list and sorts it
"""

print("sort".center(40, "-"))
l1 = [9, 5, 1, 7, 3, 8, 4, 10, 6, 2]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending :{res_desc}")

print("-" * 40)
l1 = [9, 'zebra', 5,'apple', 1, 'yellow', 7, 'blue', 3, 'violet', 8, 'pink', 4, 'green', 10, 'red', 6, 'orange', 2, 'cat', 'dog', 195, 1234, 10987, 27, 213, 2239, 20962]
print(f"l1 :{l1}")

print("-" * 40)
res = sorted(l1, key=ascii)
print(f"res :{res}")

print("-" * 40)
cities = ['thiruvananthapuram', 'bangalore', 'delhi', 'kolkota', 'hyderabad', 'pune', 'vishakapatnam', 'mumbai', 'chennai']
print(f"cities :{cities}")

print("-" * 40)
# sort the cities based on their length
res_asc = sorted(cities, key=len)
print(res_asc)

res_desc = sorted(cities, key=len, reverse=True)
print(res_desc)

print("-" * 40)
months = ['apr', 'aug', 'dec', 'oct', 'feb', 'nov', 'mar', 'jan', 'may', 'jul', 'sep', 'jun']
print(f"months :{months}")

from calendar import month_name
# print(list(month_name))
l = []

for month in list(month_name):
    l.append(month[0:3].lower())

# print(f"l :{l}")
def sort_months(mon):
    if mon in l:
        return l.index(mon)

print("-" * 40)
res = sorted(months, key=sort_months)
print(f"res  :{res}")

print('reverse'.center(40, "-"))
l1 = [9, 5, 1, 7, 3, 8, 4, 10, 6, 2]
print(f"l1 :{l1}")

res = list(reversed(l1))
print(res)
