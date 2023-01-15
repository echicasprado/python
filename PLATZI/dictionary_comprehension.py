import random
dict = {}
dict_v2 = {}
dictionary_comprehension = {}
dictionary_comprehension_v2 = {}
dictionary_comprehension_v3 = {}
new_dict = {}
countries = ['col','gt','mex','bol','pe']
names = ['nico','zule','santi']
ages = [12,56,98]

for i in range(1,11):
    dict[i] = i * 2
print(dict)

dictionary_comprehension = { e: e * 2 for e in range(1,11)}
print(dictionary_comprehension)

for e in countries:
    dict_v2[e] = random.randint(1,100)
print(dict_v2)

dictionary_comprehension_v2 = {e : random.randint(1,100) for e in countries}
print(dictionary_comprehension_v2)

print(list(zip(names,ages)))

new_dict = {name: age for (name,age) in zip(names,ages)}
print(new_dict)

dictionary_comprehension_v3 = {country : poblacion for (country, poblacion) in dictionary_comprehension_v2.items() if poblacion > 10}
print(dictionary_comprehension_v3)

# Ejemplo usando texto
text = 'Hola soy ever chicas'
unique = {c.lower() : c.upper() for c in text if c in 'aeiou'}
print(unique)
