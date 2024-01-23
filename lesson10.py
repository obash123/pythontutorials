# #  SLICING

# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Basic slicing
# subset = my_list[2:7]   # Elements from index 2 to 6 (7 is exclusive)
# print(subset)  # Output: [2, 3, 4, 5, 6]

# # Omitting start or stop
# subset_start_omitted = my_list[:5]  # Elements from the beginning to index 4
# subset_stop_omitted = my_list[5:]  # Elements from index 5 to the end
# print(subset_start_omitted)  # Output: [0, 1, 2, 3, 4]
# print(subset_stop_omitted)   # Output: [5, 6, 7, 8, 9]

# # Negative indices
# subset_negative_indices = my_list[-3:-1]  # Elements from the third-to-last to the last (exclusive)
# print(subset_negative_indices)  # Output: [7, 8]

# # Step or Stride
# subset_with_step = my_list[1:9:2]  # Elements from index 1 to 8, skipping every second element
# print(subset_with_step)  # Output: [1, 3, 5, 7]

# # Reverse the list
# reverse_list = my_list[::-1]
# print(reverse_list)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# a = matrix[0][1]
# b = matrix[1][1]
# c = matrix[2][1]
# print(a,b,c)

# # Use list slicing to get a sublist of every third element in reverse order from the list ['a', 'b', 'c', 'd', 'e', 'f', 'g'].

# list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# d = list[::-1]
# d = list[1:-1:3]
# print(d)

# # Create a list alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] and extract a sublist with every second element in reverse order.

# list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# e = list2[::-1]
# e = list2[1:-1:2]
# print(e)

# # Return every 2nd item between position 6 to 1
# L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# solution = L[6:1:-2]
# print(solution)

# list3 = [1,2,3]
# list4 = [4,5,6]
# list5 = list3 + list4
# print(list5)

# list6 = [1,2,3]
# list7 = [4,5,6]
# # list8 = list3 - list4
# # print(list8)

# #Create a string by repeating the word "Python" three times, and insert commas between the repeated words.


# word = "Python"
# thrice = (word + " ")*2 + word
# thrice = thrice.split(" ")
# thrice = ",".join(thrice)
# print(thrice)

# list1 = [1, 2, 3,7,8,9,0]
# list2 = [1, 2, 3]

# result = list1 == list2  # True if the lists are equal, False otherwise
# print(result)

# list10 = zip(list1,list2)
# print(tuple(list10))

# result1 = all(x == y for x, y in zip(list1, list2))
# print(result1)

# result2 = any(x == y for x, y in zip(list1, list2))  # True if at least one element is equal
# print(result2)

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


# learn list comprehension 
# Given the list colors = ['red', 'green', 'blue'], modify the list in a way that it becomes ['purple', 'green', 'blue'] without creating a new list.

colors = ['red', 'green', 'blue']
colors[0] = 'purple'
print(colors)

# Given a list letters = ['a', 'b', 'c', 'a', 'b', 'a'], use list methods to create a dictionary where keys are unique letters, and values are the counts of each letter.

letters = ['a', 'b', 'c', 'a', 'b', 'a']

letter_counts = {letter: letters.count(letter) for letter in set(letters)}

print(letter_counts)

# Given a list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], use list methods to partition the list into two lists: one containing odd numbers and the other containing even numbers.

odd = []
even = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("even =",even)
print("odd =",odd)


# Given a list numbers = [1, 2, 3, 4, 5], use list methods to square each element, but only if the element is greater than 2.
#list comprehension

def square():
    number = [1, 2, 3, 4, 5]
    return [ x ** 2 for x in number if x > 2]

print(square())