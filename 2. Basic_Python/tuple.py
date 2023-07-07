def multiple():
    return 3, 4
# print(multiple())

things = 'pen', 'tripped', 'water bottle', 'phone', 'web cam', 'sunglass'
# print(type(things))
print(things[0])
print(things[-2])
print(things[3:5])

if 'tripped' in things:
    print('Tripped Exist')

# things[0] = 'pen mama'

for item in things:
    print(item)