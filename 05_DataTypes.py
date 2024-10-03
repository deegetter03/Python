#Numbers (int,float,complex)
a = 10 #int (integer)
print(type(a))

b = 10.5 #float 
print(type(b))

c = 1 + 2j #complex (1+2j => x + yj)
print(type(c))

#list [] [is like array] it is also mutable[can be changed]
d = [10,10.5,20]
print(type(d))
print(d[1])

fruit = ["apple","mango","grapes"]
print(fruit[1])
fruit.insert(0,"banana")
print(type(fruit))
print(fruit)

#tuple (), immutable(cant be changed)
months = ("jan","feb","march")
print(type(months))
print(months)
#months.insert(0,"nishant")  no insert function is there for tuple

#string  ,can be written in single as well as in multiple lines
e = """nis
bro
age: 19
"""
print(type(e))
print(e)

#set {} , unique and sorts the element 
f = {1,5,6,9,2,4,4}
print(type(f))
print(f)

#dictionary : has a key : value
g = {77:"nishant",99:"kartik"}
print(type(g))
print(g)
print(g[77])