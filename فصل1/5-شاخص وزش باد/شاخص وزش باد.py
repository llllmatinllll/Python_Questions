import math
v = float(input("Input wind speed in km/h: "))
t = float(input("Input air temperature in degrees Celsius(C): "))
wci = 13.12 + 0.6215*t - 11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)
print ("The wind chill index is", int(round(wci, 0)))
