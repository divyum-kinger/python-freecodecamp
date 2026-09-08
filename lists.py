hehe = ["Roger", "Syd"]

print("Roger" in hehe)
print(hehe[0])
hehe[0] = "bobby"
print(hehe)
print(hehe[2:3])
# hehe.extend(["James", 3])
# OR
hehe += ["James", 3]
print(hehe)
print(hehe.pop()) #return last item from list
hehe.insert(2, "Test")
hehe[1:1] = ["tst1", "tst2"]
print(hehe)
itemscopy = hehe[:]

hehe.sort(key=str.lower) #this will change the list
print(sorted(hehe, key=str.lower)) #this wont change the listk
print(hehe)

# Tuples lists but these cannot be modifed
names = ("Roger", "Syd")
print(names[0])
names.index("Roger")
len(names)

print("Roger" in names)
print(sorted(names)) #wont modify the Tuple

#dictionary (hashmaps)
hehe = {"name":"Roger", "age":8}
print(hehe['name'])
