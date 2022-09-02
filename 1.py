import json
a = {123: '123'}
b = [k for k in a.keys()][0]
with open('abc.json', 'w') as file:
    file.write('{}')

with open('abc.json', 'r') as file:
    data = json.load(file)
    data = a
with open('abc.json', 'w') as file:
    json.dump(data, file, indent=4)


print(type(b))