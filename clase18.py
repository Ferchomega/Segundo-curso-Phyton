"""
a = list(range(0, 100, 2))
#print(a)

b =list(range(0,10))
#print(b)

print(a+b)
#print(b*2)

fruits = list()
fruits.append("apple")
fruits.append("banana")
#print(fruits)
#print(len(fruits))
fruits.append("kiwi")

some_fruit = fruits.pop()
#print(some_fruit)
#print(fruits)
some_fruit = fruits.pop(0)
#
# print(fruits)
"""
import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(0,15))

print(random_numbers)
ordered_numbers = sorted(random_numbers)
print(ordered_numbers)

print(dir(random_numbers))