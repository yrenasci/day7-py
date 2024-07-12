#key-value
#41 => kocaeli veya 54 => sakarya

# sehirler = ["kocaeli", "istanbul"]
# plakalar = [41, 34]
# print(plakalar[sehirler.index("kocaeli")])


#print(plakalar["kocaeli"]) => 41
#print(plakalar["istanbul"]) =>34


# plakalar = { "kocaeli":  41, "istanbul" : 34}
# print(plakalar["kocaeli"])
# print(plakalar["istanbul"])
# plakalar["kocaeli"] = "new value"
# print(plakalar)


users = {
"sadikturan" : {
"age" : 36,
"email" : "aba@gmail.com",
"phone" : "123545"
},
"yarenasci" : 2,
"email" : "yrenasci@gmail.com",
"phone" : "123123"
}
print(users["yarenasci"]["age"])