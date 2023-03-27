# #Open file for reading
f = open("song.txt")
# #Print single line of it
# print(f.readline(), end="")
# print(f.readline(), end="")
# #Print full content of the file
# print(f.read())
# #Print few characters
# print(f.read(10))
#Grab content of txt file and save it as a list
lista = f.readlines()
print(lista)
print(lista[1])
f.close()
g =open("song.txt", "a")
g.write ("\nAnd it's everlasting, infinite\n")
g.writelines(["It goes on and on, you can't measure it\n", "Can't quench your love\n"])
g.close()
