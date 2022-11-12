#Python Special Operators
#Membership operator  in and not in

PyStr="Python"
print('p' in PyStr)
print('N' not in PyStr)
print('n' not in PyStr)

x='Hello Python'
y={1:'a',2:'b'}
print('H'in x)
print('hello' not in x)
print(1 in y)
print('a' in y) # Dictionary always consider the key not the value


#Identity operator  is an is not

a=b=[1,2,3]
print(a)
print(b)
print(a is b)
c=[1,2,3]
print(a is c)
print(id(a)) # shows address of the variable
print(id(b))
print(id(c))