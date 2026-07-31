name=input("Enter student name: ")
file=open("attendance.txt","a")
file.write(name+"\n")
file.close()

file=open("attendance.txt","r")
print(file.read())
file.close()