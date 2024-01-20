# string = input("Enter any string: ")

# string = string.replace(" ","")
# print(string)

# i = 0
# j = len(string) - 1

# while True:
#     if string[i] != string[j]:
#         print("not palindrome")
#         break
#     i += 1
#     j -= 1
#     if i >= j:
#         print("palindrome")
#         break

# def sum_of_numbers(array):
#     return sum(x for x in array if x.isdigit())

# my_array = ['apple', 3, 'banana', 5, 7, 'orange', 2.5]
# result = sum_of_numbers(my_array)

# print("Sum of numbers:", result)

# def swap_case(s):
#     modified_string = ''
#     for char in s:
#         if char.islower():
#             modified_string += char.upper()
#         else:
#             modified_string += char.lower()
#     return modified_string

# input_string = "HackerRank.com presents 'Pythonist 2'"
# output_string = swap_case(input_string)
# print(output_string)

def print_full_name(first, last):
    full_name = f"Hello {first}{last}! You just delved into python."
    print(full_name)

first_name = "Ross"
last_name = "Taylor"

print_full_name(first_name, last_name)    

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

