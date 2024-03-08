#mutable
myset={1,2,3,4}
print(myset) #{1, 2, 3, 4}

myset= set("Hello")
print(myset) #prints distinguished characters
#{'e', 'o', 'H', 'l'}

myset.add(3)
print(myset) #{3, 'e', 'l', 'o', 'H'}

myset.remove("H") #or myset.discard(value)
print(myset) #{3, 'e', 'l', 'o'}



myset.pop() #prints and removes arbitrary elements from the set

print(myset) #{'e', 'l', 'o'}

# myset.clear()

for i in myset:
    print(i)

#e
#l
#o


if "o" in myset:
    print("YES") #YES


odd={1,3,5,7,9}
even={2,4,6,8}

u=odd.union(even)
print(u) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

i=odd.intersection(even)
print(i) #set()

prime={2,5,7,9}

diff=even.difference(prime)
print(diff) #{8, 4, 6}

even.update(prime)
print(even) #{2, 4, 5, 6, 7, 8, 9}
#adds elements from second set that are not present in first set

even.intersection_update(prime)
print(even) #{9, 2, 5, 7}
#takes common elements and assigns them to even


# not completed yet

