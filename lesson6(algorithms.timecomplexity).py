def find_max_element_linear(arr):
  max_element = arr[0]
  for element in arr:
    if element > max_element:
      max_element = element
  return max_element

# In the context of Big O notation, we express this algorithm’s time complexity as O(n)
# because it grows linearly with the input size. 
# This means that as the size of the array doubles, the number of operations required also approximately doubles.

def find_max_element_constant(arr):
  max_element = max(arr)
  return max_element
# In the context of Big O notation, this algorithm’s time complexity is O(1) because it exhibits constant behavior. 
# So no matter how much the input size grows, the number of operations required by the ‘find_max_element_constant’ function remains the same.

# big o from constant time to linear time like that with examples


# algorithm is a step by step way of writing instruction to solve a problem
# data structure is a way of storing or organizing algorithm in an efficient way 
# google maps uses a graph 
# breadth, depth, first search

# steps to write an efficient algorithm
# 1.  understand the problem
# 2. Choose the right data structure
# 3. Analyze the time and space complexity
# 4. Design and test the
# 4. Design and test the algorithm
# 5. Optimize the algorithm

#Create a program that asks the user for a number and then prints out a list 
#of all the divisors of that number.

# Big Oh Notation (Time Vs Input/data)
# Constant time, linear time, quadratic time, logarithmic time, binary time....

given_array = [1,4,32,4,5,6,6,7,4,3,2,2,3,5,6,6,4]

sum_num = sum(given_array)
print (sum_num)

def find_sum(given_array):
    total = 1000000 # constant time 0(1)
    for num in given_array: # linear time o(n)
        total+=num # constant time o(1)
    return total # constant time o(1)

def stupid_function(given_array):
    total = 0
    return total
x = 3
if x > 0:
    # o(logn)
    pass
elif x < 0:
    # o(logn) 
    pass
else:
    # o (log n^2) 

# o(1) + o(n) + o(1) + o(1) = o(3) + o(n)

 print(find_sum(given_array))

def quadratic_algo(arr):
    n = len(arr) # constant time
    for i in range(n): # o(n)
        for j in range(n): #o(n) * o(n) 
            print(arr[i], arr[j]) # constant time 

# therefore it's a o(n**2)
            
def sum_first_n_numbers(n):
    total = 0 # constant
    for i in range(1, n + 1): # o(n)
        total += i # constant
    return total # constant

def bubble_sort(arr):
    n = len(arr) # constant time
    for i in range(n): # o(n)
        for j in range(0, n - i - 1): # o(n**2)
            if arr[j] > arr[j + 1]:  # o(log n)
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # contant time
    return arr # constant 

# ║Name              ║ Time Complexity ║
# ╠══════════════════╬═════════════════╣
# ║ Constant Time    ║       O(1)      ║
# ╠══════════════════╬═════════════════╣
# ║ Logarithmic Time ║     O(log n)    ║
# ╠══════════════════╬═════════════════╣
# ║ Linear Time      ║       O(n)      ║
# ╠══════════════════╬═════════════════╣
# ║ Quasilinear Time ║    O(n log n)   ║
# ╠══════════════════╬═════════════════╣
# ║ Quadratic Time   ║      O(n^2)     ║
# ╠══════════════════╬═════════════════╣
# ║ Exponential Time ║      O(2^n)     ║


# Finds an item in an unsorted list
def On_simple_search(lst,number):
    is_found = False # constant time
    for num in lst: # o(n)
        if num == number: # o (log n)
            is_found = True # constant time
    return is_found # constant time

def Ologn_binary_search(list,number):
    first = 0 # constant 
    last = len(list) - 1 # constant 
    is_found = False # constant
    while first <= last and not is_found: # o(log n)
        mid = (first + last)//2 # constant
        if list[mid] == number: # o (log n)
            is_found = True # constant 
        else: # o (log n**2)
            if number < mid: # o log(n)
                last = mid - 1 # constant
            else: # o (log n**2)
                first = mid + 1 # constant
    return is_found # constant 

def merge_sort(arr):
    if len(arr) > 1: # o (log n)
        mid = len(arr) // 2 # o(1)
        left_half = arr[:mid] # o(1)
        right_half = arr[mid:] # o(1)

        merge_sort(left_half) # o(n log n)
        merge_sort(right_half) # o(n log n)

        i = j = k = 0 # o(1)

        while i < len(left_half) and j < len(right_half): # o (log n)
            if left_half[i] < right_half[j]: # o (log n)
                arr[k] = left_half[i] # o(1)
                i += 1 # o(1)
            else: # o (logn ** 2)
                arr[k] = right_half[j] # o(1)
                j += 1 # o(1)
            k += 1 # o(1)

        while i < len(left_half): # o (log n)
            arr[k] = left_half[i] # o(1)
            i += 1 # o(1)
            k += 1 # o(1)

        while j < len(right_half): # o (log n)
            arr[k] = right_half[j] # o(1)
            j += 1 # o(1)
            k += 1 # o(1)
    return arr # o(1)


nums = [1,2,3,4]

nums.insert(1,100) # --> O(n)
nums.remove(100) # --> O(n)
print (100 in nums) # ---> O(n)

nums = [1,100, 2, 3,4]

nums = [[1,2,3], [4,5,6], [7,8,9]]
for i in range(len(nums)): # --O(n)
    for j in range (nums[i]): #  --O(n^2)
        print (j) # -- O(1)


n = 5

while i < 11: # o(1)
    i += 1  # 
    print(i) # o(1)

while i < n : # o(n)
    i += 1
    print(i)  # o(1)

while i < n :  # o(n)
    i += 3
    print(i)


# suppose we have a sorted array and we want to find the index of  a particular value in the array, if it exists. 
    #What is the time complexity of the algorithm

# answer - [o (log n) - use of binary search..]
    
# learn on divide nad conquer method of programming 

n = 4
while i < n: # o(n)
    j = 0 # o(1)
    while j < (3*(n)): # o(n**2)
        j = j + 1 # o(1)
    j=0 # o(1)
    while j < 2*(n): # o(n^2)
        j = j+1 # o(1)
    i = i + 1 # o(1)

   # f(n) = o(n) + o (1) + o(n^2) + o(1) + o(1) + o(n^2) + o(1) + o(1)
    # f(n) = o(n^2)
    
n = 4
while i < 3*n: # o(n)
    j = 10 # o(1)
    while j < 50: # o(1)
        j = j + 1 # o(1)
    j=0 # o(1)
    while j < n^3: # o(n(n^3))
        j = j+2 # o(1)
    i = i + 1 # o(1)

    # f(n) = o(n) + o(1) + o(1) + o(1) + o(1) + o(n^4) + o(1) + o(1)
    # f(n) = o(n^4)
# as long as the while loop is not interacting with "n". it's going to be a constant time

