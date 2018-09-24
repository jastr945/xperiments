# any() and all() in Python
x = [True, True, True]

if any(x):
    print("At least one True")

if all(x):
    print("Not one False")

x = [True, False, True]

if any(x) and not all(x):
    print("At least one True and one False")


# collections
from collections import OrderedDict, Counter

# Remembers the order the keys are added!
ordered = OrderedDict(a=1, b=2, c=3)

# Counts the frequency of each character
counted = Counter("Hello World!")

print(ordered, counted)


# **kwargs
dictionary = {"a": 1, "b": 2}

def someFunction(a, b):
    print(a + b)
    return

someFunction(**dictionary)


# list comprehension
cities = ['London', 'Dublin', 'Oslo']

def visit(city):
    print("Welcome to " + city)

for city in cities:
    visit(city)


# map() and lambda
x = [1, 2, 3]
y = map(lambda x : x + 1 , x)

# prints out [2,3,4]
print(list(y))


# operator overloading
class Thing:
    def __init__(self, value):
        self.__value = value
    def __gt__(self, other):
        return self.__value > other.__value
    def __lt__(self, other):
        return self.__value < other.__value

something = Thing(100)
nothing = Thing(0)

# True
print(something > nothing)

# False
print(something < nothing)

# Error
#something + nothing


# pprint
import requests
import pprint

url = 'https://randomuser.me/api/?results=1'
users = requests.get(url).json()

pprint.pprint(users)


# sh library
import sh

print(sh.pwd())
#sh.mkdir('new_folder')
#sh.touch('new_file.txt')
print(sh.whoami())
print(sh.echo('This is great!'))
