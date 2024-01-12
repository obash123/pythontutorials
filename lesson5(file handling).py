#strings = []
with open('strings.txt', 'r') as file:
    strings = [line.strip() for line in file]

    # for line in file:
    #     #print (line)
    #     strings = [line.strip()]
    #     print(strings)

#print(strings)

def counter(Ul):
    count = 0
    for i in Ul:
        if i.isupper():
            count += 1
    return count

# def counter(s):
#     return sum(1 for char in s if char.isupper())

sorted_strings = sorted(strings, key=counter)

print(sorted_strings)

with open('sortedstrings.txt', 'w') as output_file:
    for string in sorted_strings:
        output_file.write(f"{string}\n")


# one line loops 
# read and write 
# classes
# sorting 
# strip
        

