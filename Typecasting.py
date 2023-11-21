a = 10
b = 20
a,b = b,a
print(a,b)

print(type(a))
a = float(a)
print(a)
print(type(a))

a = str(a)
print(type(a))
print(a)

a = 10.1
b = 20.2
a,b = b,a
print(a,b)
print(type(b))

b= complex(a)
print(b)

b= complex(a,4)
print(b)

#Immutable data type

a=10
b=10
print(id(a))
print(id(b))

print(a is b)
