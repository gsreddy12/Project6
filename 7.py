#Ternary operator
a,b=10,20
c=a if a<b else b
print(c)
d=a if a>b else b
print(d)

#Nesting of Ternary operator also possible

x=int(input("Enter any Number :"))
y=int(input("Enter any Number :"))
z=int(input("Enter any Number :"))
Min=x if x<y and x<z else y if y<z else z
Max=x if x>y and x>z else y if y>z else z
print(Min)
print(Max)