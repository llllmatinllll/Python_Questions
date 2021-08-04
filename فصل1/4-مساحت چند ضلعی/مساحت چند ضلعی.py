from math import tan, pi
nsides = int(input("Input number of sides: "))
slength = float(input("Input the length of a side: "))
parea = nsides * (slength ** 2) / (4 * tan(pi / nsides))
print("The area of the polygon is: ",parea)
