import math

def center_of_square(x1, y1, width, height):
    x2 = x1 + width
    y2 = y1 + height
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    return center_x, center_y

x1 = float(input("Enter x coordinate : "))
y1 = float(input("Enter y coordinate : "))
width = float(input("Enter width: "))
height = float(input("Enter height: "))

def center_of_square2(x10, y10, width10, height10):
    x20 = x10 + width10
    y20 = y10 + height10
    center_x2 = (x10 + x20) / 2
    center_y2 = (y10 + y20) / 2
    return center_x2, center_y2

x10 = float(input("Enter x coordinate : "))
y10 = float(input("Enter y coordinate : "))
width10 = float(input("Enter width: "))
height10 = float(input("Enter height: "))

def distance_between_squares(x1, y1, width, height, x10, y10, width10, height10):
    center_1 = center_of_square(x1, y1, width, height)
    center_2 = center_of_square2(x10, y10, width10, height10)
    distance = math.sqrt((center_2[0] - center_1[0]) ** 2 + (center_2[1] - center_1[1]) ** 2)
    return distance

print(distance_between_squares(x1, y1, width, height, x10, y10, width10, height10))