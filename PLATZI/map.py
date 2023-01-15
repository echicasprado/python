numbers = [1,2,3,4]
numbers_v2 = []
numbers_v3 = []

for i in numbers:
    numbers_v2.append(i * 2)

numbers_v3 = list(map(lambda x: x * 2,numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

numbers = [1,2,3,4]
numbers_v2 = [5,6,7]
numbers_v3 = list(map(lambda x, y: x + y,numbers,numbers_v2))

print(numbers)
print(numbers_v2)
print(numbers_v3)

#### MAP WITH DICTIONARYS
items = [
    {'product':'camisa',
     'price':100
     },
    {'product':'camisa 2',
     'price':300
     },
    {'product':'camisa 3',
     'price':200
     }
]

prices  = list(map(lambda item: item['price'], items))
print(prices)

def add_taxes(item):
    new_items = item.copy()
    new_items['taxes'] = new_items['price'] * .17
    return new_items

new_items = list(map(add_taxes, items))
print('OLD LIST')
print(items)
print('NEW LIST')
print(new_items)