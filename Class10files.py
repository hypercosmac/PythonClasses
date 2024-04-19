
file = open("testfile.txt","w")
file.write("This is my first file created using Python")
file.write("\nSecond line")
file.close()

f2 = open("testfile.txt","r")
print(f2.read())
f2.close()
