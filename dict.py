a={

    "sarik":43,
    "nakul":21,
    0:3,
    1:10
}

print(a)
print("sarik")
a.update({"sarik":100})
print(a.items())
print(a["sarik"])
print(a.get("sarik"))
 #dictionary is mutable 
#  it is indexable

a.clear()
print(a)


a.update({0:1})
a.update({"sarik":1})
print(a)

print(a.values())
print(a.keys())