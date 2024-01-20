# def f(x):
#     return (x + 1) 

# def g(x):
#     return (x + 1)  

# def double_func(f, g):
#     def h(x):
#         return f(g(x))
#     return h

# h = double_func(f, g)

# result = h(3)
# print(result)

def generate_pascals_triangle(rows):
    triangle = []

    current_row = 0
    while current_row < rows:
        row = [1]

        i = 1
        while i < current_row:
            row.append(triangle[current_row - 1][i - 1] + triangle[current_row - 1][i])
            i += 1

        if current_row > 0:
            row.append(1)

        triangle.append(row)
        current_row += 1

    return triangle

# Set the number of rows you want in Pascal's Triangle
num_rows = int(input("how many do you want: "))
result = generate_pascals_triangle(num_rows)

# Print the result
for row in result:
    print(row)


