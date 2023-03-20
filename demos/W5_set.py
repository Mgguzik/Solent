#Initialise empty set
s = set()
#Initialise non empty set
colours= {"blue", "red", "yellow", "purple", "red"}
print(colours)
#print(len(colours))
#Adding elements into a sets
colours.add("green")
colours.add("navy blue")
print(colours)
#Adding multiple elements to a set
colours=colours.union({"black", "turquise", "crimson", "magenta"})
print(colours)
#Remove items from a set
if "yellow" in colours:
    colours.remove("yellow")
print(colours)
#Sets are heterogenous- can accept multiple data types, duplicates are not allowed
colours.add(99)
colours.add(True)
print(colours)
print(type(True))
#Check membership
if "yellow" in colours:
    print("Yay- I like yellow")
else:
    print("Sad days- no yellow!")

c = {"brown", "turquise","cyan", "coquelicot", "pink", "red"}
#Union- joining two sets together, not keeping duplicates (each element apppears one time)

c2 = colours.union(c)
print(f"c is {c}")
print(f"c2 is {c2}")
print(f"colours is {colours}")

#Intersection- looking at common values of two collections
c3= c.intersection(colours)
print(f"c3 is {c3}")

#Difference- keep elements of one set that are not part of the other
c4= colours.difference(c)
c5=c.difference(colours)
print(f"c4 is {c4}")
print(f"c5 is {c5}")

#DICTIONARY
#Initialise empty dictionary
d = {}
#Initiaise non-empty dictionary
phonebook = {"Thomas":7765431783, "Aga":788792912, "MD":7777277723}
#Print full dictionary
print(phonebook)
#Print/access individual elements
name= input("Who you gonna call: ")
if name in phonebook:
    print(f"Callin...{phonebook[name]}")
else:
    print(f"No number for {name}")
#Zipping two list together to compose a dictionary
names= ["Garry", "Ian", "Laura"]
age= [56,21,16]
people= dict(zip(names, age))
print(people)

#Traversing dictionaries- accesing keys/values/both
for thing in people:
    print(thing)
for thing in people.values():
    print(thing)
for thing in people.keys():
    print(thing)
for k, v in people.items():
    print(f"Person {k} is {v} years old")

