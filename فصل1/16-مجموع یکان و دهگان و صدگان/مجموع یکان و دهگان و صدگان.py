n = int(input("Input an Integer : "))

n1 = int("%s" % n)
n2 = int("%s%s" % (n,n) )
n3 = int("%s%s%s" % (n,n,n))

print (n1, " + ", n2," + ", n3, " = ", n1+n2+n3)
