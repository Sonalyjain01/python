"""
#set default function
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)
"""
"""
#fromkeys function
x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)
# keys for the dictionary
alphabets = {'a', 'b', 'c'}

# value for the dictionary
number = 1

# creates a dictionary with keys and values
dictionary = dict.fromkeys(alphabets, number)

print(dictionary)

# Output: {'a': 1, 'c': 1, 'b': 1}
"""
#copy function
a={
    1:11,
    2:22
    }
b={
    3:33,
    4:44
    }
c=a
print(a)
print(b)
print(c)
c=a.copy()
print(a)
print(b)
print(c)
a[6]=66
print(a)
print(b)
print(c)

print(b)
