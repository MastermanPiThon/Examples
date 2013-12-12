print ("Hello Python")

a = 5;
b = a * a;

print ("b={}".format (b))

c = [a, b]
print (c)

d = c

d[0] = "Hello"

print (c)

e = d[:]

e[1] = "Banana"

print ("e={}".format (e))
print ("c={}".format (c))
