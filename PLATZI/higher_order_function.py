def increment(x):
    return x + 1

def high_ord_func(x,func):
    return x + func(x)

print(high_ord_func(1,increment))

### USANDO LAMBDA
increment_v2 = lambda x: x + 1
print(high_ord_func(2,increment_v2))
print(high_ord_func(2,lambda x: x * 2))