from math import pi

def find_area_perimeter(shape):
    AP = [None for i in range(2)]
    if shape == 'C':
        #assume the user inputs an integer
        rad = int(input("What is the circle radius?"))
        AP[0] = round(pi*(rad**2),4)
        AP[1] = round(2*pi*rad,4)
    elif shape == 'R':
        #assume the user inputs an integer for both length and breadth
        l = int(input("Rectangle length?"))
        b = int(input("Rectangle breadth?"))
        AP[0] = l*b
        AP[1] = (2*l) + (2*b)
    elif shape == 'S':
        #assume the user inputs an integer
        s = int(input("Square side length?"))
        AP[0] = s*s
        AP[1] = 4*s
    else:
        print("Please type 'C', 'R', or 'S'")
        return 0
    return AP

user_shape = input("Choose a shape: (C)ircle or (R)ectangle or (S)quare")
shape_info = find_area_perimeter(user_shape)
if shape_info != 0:
    print("Area:", shape_info[0], "square units and Perimeter:", shape_info[1], "units")
        
