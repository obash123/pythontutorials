my_list = [9,8,"pig","capybara",9,True,"p","a","b",'a']

# my_list[0] = 100     # Update the first element
# my_list.append('d')  # Add a new element at the end
# del my_list[2]       # Remove the element at index 2

# my_list.append(4)        # Add an element at the end
#my_list.extend([5, 6])   # Extend the list with another list
#my_list.insert(2, 'x')   # Insert 'x' at index 2
#my_list.remove('a')      # Remove the first occurrence of 'a'
# popped_element = my_list.pop()   # Remove and return the last element
# print(my_list.count('a'))



# def square():
#     list1 = []
#     for i in range(5):
#         list1.append(i**2)
#     return list1
    

# def sqd():
#     return [ x**2 for x in range(5)]
    
# print(square())
# print(sqd())



# list3 = [1,4,6,8,9]
# print(max(list3))
# print(min(list3))
# print(sum(list3))
    
# list4 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# # print(dir(list4))

# print(sorted(list4)) # it sorts  in ascending order
# print(list4)

# subset = my_list[1:4]   # Elements from index 1 to 3 (exclusive)
# print(subset)

# my_list[1] = 100
# print(my_list)


def merge():
    list5 = [3,6,9,8,4]
    list6 = [0,700,2,0]
    s1 = sorted(list5)
    print(s1)
    s2 = sorted(list6)
    print(s2)
    s1.extend(s2)
    return sorted(s1)

print(merge())


name = ["oba",'kemi','feyi','towi','ninma','adam']
list7 = []
for letter in name:
    if letter[0] in "aeiou":
        list7.append(letter)
print(list7)

# Write a function that takes two lists and returns a new list containing only the common elements.
# Sort a list of strings based on the frequency of characters in each string.


def common(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    return common_elements

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = common(list1, list2)
print(result)
 
