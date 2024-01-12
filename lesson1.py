# for loop 

books = ["Maths", "English", "Phyiscs"]

vehicle = ("Toyota","BMW","Nissan")

churches = {
    "orthodox":"Anglican",
    "pentecostal":"Winners",
    "methododist":"Baptist"
}

print(type(books))
print(type(vehicle))
print(type(churches))

# dir allows you to find out the methods available for a data type
print(dir(books))


for book in books:
    print(book)

for church in churches:
    print(church)

numbers = [2,5,6,7,4,3,5,7,8,9,5,6,73,2,7,4,7890,0]

sum = 0 
for num in numbers:
    sum += num  
print (sum)

for i in range(100):
    print(i)
    
for i in range(0,100,5):
    print(i)