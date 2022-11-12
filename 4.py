#Logical(Boolean) Operator

x=True
y=False
print(x and y)
print(x or y)
print(not y)
print(not x)

x=0
y=1
print(x and y)
print(x or y)
print(not y)
print(not x)

x=''
y=True
print(x and y)
print(x or y)
print(not y)
print(not x)

x='Hello'
y='Sateesh'
print(x and y)
print(x or y)
print(y and x)
print(y or x)

#repr() - printable representation
x="Hello Python"
print(repr(x))

x=""
y="world"
print(repr(x and y))
print(repr(y and x))
print(repr(x or y))
print(repr(y or x))
print(repr(not x))
print(repr(not y))