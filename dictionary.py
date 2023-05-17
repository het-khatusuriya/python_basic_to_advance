dic ={
    "name": "het khatsuriya",
    "id": "101"
}
print(dic)
print(dic.get('name'))


print(dic.items())

for key, value in dic.items():
    print(f"the value corresponding to the key {key} is {value}")



#methods of dictionary
print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.get('name'))
print(dic.pop('name'))

ep1 ={
    122: 45,
    123: 56,
    124: 67,
}

ep2 ={
    222:67,
    224:68,
    225:69
}
ep1.update(ep2)

del ep1[122]
print(ep1)