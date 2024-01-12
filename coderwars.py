def better_than_average(class_points, your_points):
    class_average = sum(class_points) / len(class_points)
    return your_points > class_average

class_points = [2,3]
your_points = 5
    
result = better_than_average(class_points, your_points)
print(result)