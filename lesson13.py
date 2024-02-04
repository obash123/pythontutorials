# thislist = [100, 50, 65, 82, 23]

# def myfunc(n):
#   return abs(n - 50)

# thislist.sort(key=myfunc)
# print(thislist)





# # this_list = [100, 50, 65, 82, 23]
# # this_list.sort(reverse = True)
# # print(this_list)

# # Sort the list based on how close the number is to 50:
# # def my_func(n):
# #   return abs(n - 50)

# # thislist = [100, 50, 65, 82, 23]

# # thislist.sort(key = my_func)

# # print(thislist)


# # The absolute differences between each element and 50 are [50, 0, 15, 32, 27].
# # The sorted list is based on these differences in ascending order: [0, 15, 27, 32, 50].
# # Therefore, the final sorted list is [50, 65, 82, 23, 100].

# # sorting according to the second item in each tuple
# pairs = [(1, 5), (3, 2), (2, 8), (4, 1)]

# def func(n):
#   return n[1]

# pairs.sort(key = func)
# print(pairs)


# # sorting according to the length of each word
# words = ["apple", "banana", "orange", "kiwi", "grape"]

# def function(l):
#   return len(l)

# words.sort(key = function)
# print(words)

# # sorting according to the sum of each list
# lists = [[3, 1, 4], [1, 5, 9], [2, 6, 5], [3, 5, 8]]

# def summation(n):
#   return sum(n)

# lists.sort(key = summation)
# print(lists)

# answer = sorted(lists,key = summation, reverse= True)
# print(answer)

words = ["hello", "world", "python", "programming", "language"]

def vowel(n):    
    print(n)
    count = 0
    for letters in n:
        if letters in "aeiou":
            count += 1
    return count
  
words.sort(key = vowel, reverse = True)
print(words)

def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

words = ["hello", "world", "python", "programming", "language"]
sorted_words = sorted(words, key=count_vowels)
print(sorted_words)


# Output: ['world', 'python', 'language', 'hello', 'programming']
     

# name = ["oba",'kemi','feyi','towi','ninma','adam']
# list7 = []
# for letter in name:
#     if letter[0] in "aeiou":
#         list7.append(letter)
# print(list7)

# check on the filter function, lambda, make old assignment a class, website practice


# 1
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False
 
 
# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
 
# using filter function
filtered = filter(fun, sequence)
 
print('The filtered letters are:')
for s in filtered:
    print(s)

seq = [0, 1, 2, 3, 5, 8, 13]


 
#2
# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
 
# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))

# 3

# Define a function to check 
# if a number is a multiple of 3
def is_multiple_of_3(num):
    return num % 3 == 0
 
 
# Create a list of numbers to filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
# Use filter and a lambda function to
# filter the list of numbers and only
# keep the ones that are multiples of 3
result = list(filter(lambda x: is_multiple_of_3(x), numbers))
 
# Print the result
print(result)


