numbers = []
numbers_v2 = []
numbers_list_comprhension = []
numbers_list_comprhension_v2 = []

for e in range(1,11):
    numbers.append(e * 2)
print(numbers)

numbers_list_comprhension = [e for e in range(1,11)]
print(numbers_list_comprhension)

numbers_list_comprhension = [e * 2 for e in range(1,11)]
print(numbers_list_comprhension)

for e in range(1,11):
    if e % 2 == 0:
        numbers_v2.append(e * 2)
print(numbers_v2)

numbers_list_comprhension_v2 = [e for e in range(1,11) if e % 2 == 0]
print(numbers_list_comprhension_v2)

numbers_list_comprhension_v2 = [e * 2 for e in range(1,11) if e % 2 == 0]
print(numbers_list_comprhension_v2)