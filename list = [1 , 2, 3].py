list = [1 , 2, 3]

tuple = (1, "iki", 3)
print(type(list))
print(type(tuple))
print(list[1])
print(tuple[2])

print(len(tuple))
print(len(list))
list[0] = "ahmet"
#tuple[0] = "deniz" #herhangi bir elemana değişim/atama yapılmıyor
list =["ali", "veli"]
tuple = ("damla" , "ayşe", "ayşe")
names = ("damla", "yaren", "tutu") + tuple
print(names)
print(list)
print(tuple)

print(tuple.count("ayşe"))