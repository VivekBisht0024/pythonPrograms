f = open("newFile.txt" , 'r')
print(f.read())
print(f.readline())
f = open('newFile.txt' , 'w')
f.write("Hello World")


print(f)

f.close()

f = open("newFile.txt" , 'a')
f.write("Hey Brother I'm vivek bisht")
print(f.read())




