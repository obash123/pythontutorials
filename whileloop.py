# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# count = 1
# while count <= 10:
#     print(count * 3)
#     count += 1

# for number in range(10):
#     if number == 5:
#         break
#     print(number)

# for number in range(10):
#     if number == 5:
#         continue
#     print(number)


count = 1
while count <= 20:
    if count % 2 == 0:
        count += 1
        continue
    print(count * 5)
    count += 1

def is_prime(num):
    if num <= 1:
        return False

    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            return False
        divisor += 1

    return True

n = int(input("Enter a number: "))

if is_prime(n):
    print(" prime number.")
else:
    print("not a prime number.")


