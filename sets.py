s=set()   #empty set
l={}      #empty dictinory
#sets is unordered whereas list is ordered
#no repitition is allowed
#sets are unindexed
# sets are mutable

o={1,2,3,4,5,6,"sarik"}
print(o)
o.remove(1)
print(o)
o.pop()
print(o)
p={1,9}
print(o.issubset({1,2,3,4,5,6,7,8,9,20}))
print(o.issuperset({1,2,3,4,5,6,7,8,9,20}))
print(o.union(p))
print(o.intersection(p))
o.clear()
