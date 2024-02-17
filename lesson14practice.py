# '''
# Write a program that takes a list of words as input 
# and produces a dictionary containing the frequency of each unique word.
# '''

# word_list = ["how","are","you","doing","today",",","are","you","doing","well","?"]

# letter_counts = {word: word_list.count(word) for word in set(word_list)}

# print(letter_counts)

# '''
# Write a function that takes a list of strings and groups anagrams together. An anagram is a word or phrase formed by rearranging the letters of another.

# 4:36                      PM
# word_list = ["listen", "silent", "enlist", "heart", "earth", "threa"]

# # Output: [['listen', 'silent', 'enlist'], ['heart', 'earth', 'threa']]
# '''
# list1 = ["listen", "silent", "enlist", "heart", "earth", "threa"]

# def anagram(list1):
#     empty_dict = {}
#     for word in list1:
#         sorted_word = ''.join(sorted(word))
#         if sorted_word in empty_dict:
#             empty_dict[sorted_word].append(word)
#         else:
#             empty_dict[sorted_word] = [word]

#     return empty_dict

# print(anagram(list1))

# '''
# Implement a function that determines if there exists a subset of a 
# given list whose sum is equal to a specified target value.

# Given a list of positive integers and a target sum,
# write a function to determine whether there exists a 
# subset of the integers that adds up to the given target.

# numbers_list = [3, 7, 1, 8, 5]
# target_sum = 12
# result = the_function(numbers_list, target_sum)
# print(result)
# # Output: True (since 3 + 1 + 8 = 12)
# '''

# numbers_list = [3, 7, 1, 8, 5]
# def the_function(numbers_list, target_sum):
#     num_length = len(numbers_list)

#     for i in numbers_list:
#         if target_sum < i:
#             print("there's no sum that adds up to",target_sum)
#         else:

# print(numbers_list)
# target_sum = 12
# result = the_function(numbers_list, target_sum)
# print(result)


def is_subset_sum(nums, target):
    def backtrack(start, target):
        if target == 0:
            return True
        if target < 0 or start >= len(nums):
            return False

        # Try including the current element in the subset
        if backtrack(start + 1, target - nums[start]):
            return True

        # Try excluding the current element from the subset
        if backtrack(start + 1, target):
            return True

        return False

    return backtrack(0, target)


# Test the function
nums = [3, 34, 4, 12, 5, 2]
target = 9
print(is_subset_sum(nums, target))  

