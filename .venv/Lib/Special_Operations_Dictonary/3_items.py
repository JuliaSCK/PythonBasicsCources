d1 = {
    "Omer": 25,
    "Yuval": 10,
    "Oren": 12,
    "Guy": 54,
    "Ilanit": 32
}

print(d1.items())
print(type(d1))
print(type(d1.items()))

# print(d1.items()[0]) - Output: TypeError: 'dict_items' object is not subscriptable

print(list(d1.items()))
print(list(d1.items())[0])
print(type(list(d1.items())[0]))