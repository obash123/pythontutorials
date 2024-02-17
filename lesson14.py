# # 1
# x = lambda a : a + 10
# print(x(5))

# x = lambda a, b : a * b
# print(x(5, 6))

# def fun(variable):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if (variable in letters):
#         return True
#     else:
#         return False
 
 
# # sequence
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
 
# # using filter function
# filtered = filter(fun, sequence)
 
# print('The filtered letters are:')
# for s in filtered:
#     print(s)

# seq = [0, 1, 2, 3, 5, 8, 13]


 
# #2
# # result contains odd numbers of the list
# result = filter(lambda x: x % 2 != 0, seq)
# print(list(result))
 
# # result contains even numbers of the list
# result = filter(lambda x: x % 2 == 0, seq)
# print(list(result))

# # 3

# # Define a function to check 
# # if a number is a multiple of 3
# def is_multiple_of_3(num):
#     return num % 3 == 0
 
 
# # Create a list of numbers to filter
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
# # Use filter and a lambda function to
# # filter the list of numbers and only
# # keep the ones that are multiples of 3
# result = list(filter(lambda x: is_multiple_of_3(x), numbers))
 
# # Print the result
# print(result)


# ENUMERATE helps to return the index value of every item in the list
# fruits = ["apple", "banana", "orange", "kiwi"]
# indexed_fruits = list(enumerate(fruits, start = 1))
# print(indexed_fruits)
# Output: [(1, 'apple'), (2, 'banana'), (3, 'orange'), (4, 'kiwi')]


# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x**2, numbers))
# print(squared_numbers)
# Output: [1, 4, 9, 16, 25]

#Given a list of tuples where each tuple represents a pair of (name, age), 
#create a function named filter_adults using the filter function to 
#return only the pairs where the age is 18 or older.

# list1 = [('obasola',17),('ore',17),('Gomez',32),('sunny',4),('batman',23),('peter',31),('baudelaire',14)]

# def filter_adults(n):
#     if n[1] >= 18:
#         return n[1]

# # answer = filter(filter_adults,list1)
# # print(list(answer))

# # x = lambda a : a + 10
# # print(x(5))

# Filter_adults = list(filter(lambda n : n[1] >= 18,list1))
# print(Filter_adults)

'''
Write a function named find_consecutive_pairs that takes a list of integers,
and uses the enumerate function to return a list of tuples, 
each containing a pair of consecutive integers and their indices in the original list. 
If there are no consecutive pairs, the function should return an empty list.
The function find_consecutive_pairs should use enumerate to iterate through the list,
and identify consecutive pairs of numbers along with their indices.
The result should be a list of tuples, where each tuple contains three elements: 
the pair of consecutive numbers and their index in the original list.
If there are no consecutive pairs, the function should return an empty list.
'''

# collect a list of numbers
# iterate and find consecutive pairs of numbers 
# get their indexes 
# if there are consecutive numbers, return a list of tuples with the consecutive numbers and their index
# if there aren't any consecutive numbers, return an empty list 


# def find_consecutive_pairs(numbers_list):
#     consecutive_pairs = []

#     for i, num in enumerate(numbers_list[:-1]):
#         print(num)
#         next_num = numbers_list[i+1]
#         if next_num - num == 1:
#             consecutive_pairs.append((num, next_num, i))
#     return consecutive_pairs
#         #if list_pair[i] == list_pair[i+1]:

# numbers_list = [1, 2, 3, 7, 5, 6, 8, 9, 11, 12]   
# # print(numbers_list[:-1])    
# print(find_consecutive_pairs(numbers_list))


'''
Write a function named find_local_maxima that takes a list of integers 
and uses the enumerate function to return a list of tuples, 
each containing a local maximum and its index in the original list.
A local maximum is defined as an element that is strictly greater than its neighboring elements.
The function find_local_maxima should use enumerate to iterate through the list
and identify local maxima along with their indices.
A local maximum is an element greater than both its neighbors.
The result should be a list of tuples, where each tuple contains two elements: 
the local maximum and its index in the original list.
'''

# collect  a lsit of numbers 
# iterate through it 
# return a tuple containing a locak maximum 
# local max has to be greater than both neighouring elements
# return local max and index 


def find_local_maxima(numbers_list):
    consecutive_pairs = []

    for i, num in enumerate(numbers_list[:-2]):
        # print(num)
        next_num = numbers_list[i+1]
        upper_num = numbers_list[i+2]
        if next_num - num >= 1 and next_num - upper_num >= 1:
            consecutive_pairs.append((next_num, i + 1))
    return consecutive_pairs
        #if list_pair[i] == list_pair[i+1]:

numbers_list = [3, 1, 4, 7, 2, 9, 5] 
# print(numbers_list[:-1])    
print(find_local_maxima(numbers_list))

import math
print(math.degrees(math.pi / 2))
print(round(6.5))