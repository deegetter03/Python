#int + int = int
#int + float = float
#float + float = float
#float + int = float

#str + int = error
#str + float = error

'''Implicit type conversion :- python automatically convert one data type to another '''

a = 10 #int
b = 20.3 #float
c = b + a 
print(type(c)) #syntax to know the data type
print(c)

#Explicit type conversion :- user convert datatype

m = 100
n = "40"
n = int(n) # user conversion explicit
p = m + n
print(type(p))
print(p)