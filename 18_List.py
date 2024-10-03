# Python list is used store multiple items in ordered form,are mutable(can be changed)

#empty list
a_list = []
print(a_list)

#list of int
a_int = [1,2,3,4,5]
print(a_int)

#list of float
a_float = [1.0,2.2,3.4,3.5]
print(a_float)

#list of string
a_str = ["apple","mango","grapes"]
print(a_str)

#list with mixed data types
a_mix = [1,1.0,"apple"]
print(a_mix)

a_mix = [1,1.0,"apple"]
#access list items
print(a_mix[0])
print(a_mix[1])
print(a_mix[2])

#nested list
nest_list = ["hello",[1,2,3]]
print(nest_list[0])
print(nest_list[1][0]) #1
print(nest_list[1][1]) #2
print(nest_list[1][2]) #3

#negative indexing
a = [1,2,3,4,5]
print(a[-1]) #5 ,last/piche se indexing
print(a[-2]) #4

#to find length of a list
a = [1,2,3,4,5,6,7,8,9,10]
print(len(a))

# List Methods -> append(), extend(), index(), insert(), count(), remove(), pop(), reverse(), sort().

# append() -> adds to the last of list
fruit = ["apple", "mango"]
print(fruit)
fruit.append("banana")
print(fruit)

#extend() -> extends the list and add both or merge
lang = ["eng", "hindi"]
lang1 = ["french","german"]
lang.extend(lang1)
print(lang)

#index() -> tells the position
lang1 = ["french","german"]
print(lang1.index("german"))

#insert() -> inserts in list
lang1 = ["french","german"]
lang1.insert(1,"hindi")
print(lang1)

#count() -> counts the occurrence in list
list_int = [1,2,3,1,1,1,2,2]
print(list_int.count(1))
print(list_int.count(3))

#remove() -> remove the item by name from the list
lang = ["french","german"]
lang.remove("french")
print(lang)

#pop() -> remove the item by index
lang = ["french","german"]
lang.pop(1)
print(lang)

#reverse() -> reverse the items in list
lang = ["french","german"]
lang.reverse()
print(lang)

#sort() -> sort the item in list
list_int = [1,5,3,6,1,2,4,5,23,5]
list_int.sort()
print(list_int)

#sort in reverse
list_int.sort(reverse=True)
print(list_int)