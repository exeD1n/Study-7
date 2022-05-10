import os

path = "dirs"

sto = 0
dva = 0
tri = 0

list_fiels = {}

for i in os.listdir(path):
    if os.path.getsize(path + "//" + i) < 100:
        sto += 1
        list_fiels["100"] = sto
    if 1000 > os.path.getsize(path + "//" + i) > 100:
        dva += 1
        list_fiels["1000"] = dva
    if os.path.getsize(path + "//" + i) > 1000:
        tri += 1
        list_fiels["∞"] = tri
print(list_fiels)
