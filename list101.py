def func(list_1):
    list_1[0] = 888


def func2(list_1=[1, 2]):
    list_1.append(100)
    return list_1


first: list = ["a", "b", "c", "d", "e", True]
# Index from 0 etc

print(first[4])

first[0] = 1_000_000
print(first[0])
print(first)

print(first[-1], first[-2], first[-6])

first.append(5)
print(first)

first.pop()
print(first)

removed = first.pop(2)  # c gone
print(removed, first)

first.remove("d")  # d gone
print(first)

try:
    first.remove("X")  # not exist
except ValueError:
    print("Nope....not in list")

first.insert(2, 2000)
print(first)

first.append(['what', 'else...'])  # add as listLis
print(first)

first.extend(['what', 'else...'])  # add as individual items
print(first)

# Mutability
tup = (1, 2, 3)  # immutable after created
# Not available....tup[0] = 100  #
second = first
second[0] = 21766
print(first, second)  # both have 21766

# Best way
second = first.copy()
second[0] = 999
print(first, second)  # second now separate list

three = [1, 2, 3]
func(three)
print(three)  # now 888

first = [
    [1, 2],
    [3, 4]
]
print(first[0][0:])  # all items from 0
print(first[1][0:])  # all items from 1
print(first[0])  # all items from 0 as above
print(first[1])  # all items from 1 as above
print(first)  # all items

lst1 = func2()
lst2 = func2()
lst3 = func2()
print(lst1, lst2, lst3)

lst1 = func2([])  # override default set
lst2 = func2([])
lst3 = func2([])
print(lst1, lst2, lst3)  # just 100

# Slicing
first = [1, 2, 3, 4, 5, 6, 7, 8]
print(first[:])  # copy of the list - show all items
print(first[:2])  # Just pos 0 and 1
print(first[2:])  # from pos 2 until end
print(first[1:6])  # from pos 1 up to but not include pos 6
print(first[1:8:2])  # has a step of 2 - so 2, 4, 6, 8
print(first[0:9:3])  # has a step of 3 - so 1, 4, 7
print(first[:-1])  # all items except last
print(first[-1:])  # just last - 8
print(first[::-1])  # reverse order full list
first[2:4] = [19, 20]  # add 19, 20 at pos 2
print(first)

# Useful methods
first = [9, 7, 11, 1, 2, 3, 4, 5, 5, 6, 7, 8, "Paul"]
contains_4 = "Paul" in first  # True
index = first.index("Paul")
print(contains_4, index)
print(first.count(5))  # 2
first = [9, 7, 11, 1, 2, 3, 4, 5, 5, 6, 7, 8]
first.sort()
print(first)
first.sort(reverse=True)
print(first)
first.reverse()
print(first)
print(list(reversed(first)))

# copy
first = [9, 7, 11, 1, 2, 3, 4, 5, 5, 6, 7, 8, "Paul"]
second = first[:]
second[0] = 888
print(first, second)

# zip
first = ['Paul', 'Rory', 'Caitlin']
ages = [40, 19, 22]
zipped = zip(first, ages)
print(list(zipped))  # created tuples name/age in list

# list comprehension
first = [x for x in range(10)]
print(first)
first = [x for x in range(10) if x % 2 == 0]  # 2 4 6 8
print(first)
first = [[x for x in range(10) if x % 2 == 0] for _ in range(5)]  # even numbers 5 times
print(first)