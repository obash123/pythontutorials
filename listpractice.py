# check the functionalities of lists, zip, extend, map, pop,insert, sorted. diff between sort and sorted 

# append(x): Adds an element x to the end of the list.

# extend(iterable): Appends elements from an iterable to the end of the list.

# insert(i, x): Inserts element x at the specified index i.

# remove(x): Removes the first occurrence of element x from the list.

# pop([i]): Removes and returns the element at index i (or the last element if no index is provided).

# index(x[, start[, end]]): Returns the index of the first occurrence of element x in the list.

# count(x): Returns the number of occurrences o
# copy(): Returns a shallow copy of the list.
# those are list methods

list1 = [1,2,3,4,5,6,7]
list2 = [8,9,10,11,12,13,14,10]

print(list1.pop(5))
print(list1)

print(list2.count(10))

print(list2.index(10))

print(list1.insert(5,10))
print(list1)

answer = zip(list1,list2)
print(set(answer))


def addition(n):
    return n + n

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))