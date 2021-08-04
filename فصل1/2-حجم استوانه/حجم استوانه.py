pi = 3.14
height = float(input("Enter height of cylinder: "))
radius = float(input("Enter radius of cylinder: "))
volume = ((radius * radius) * pi) * height
surarea = ((2*pi*radius)*height) +(2*(pi * radius ** 2))
print("Volume is: ", volume)
print("Surface Area is: ", surarea)
