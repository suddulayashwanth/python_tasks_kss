file=open("employees.txt","r")
highest=""
salary=0

for line in file:
    print(line.strip())
    data=line.split()
    if int(data[1])>salary:
        salary=int(data[1])
        highest=data[0]

file.close()

print("Highest Salary Employee =",highest)
print("Salary =",salary)

name=input("Enter employee name: ")
pay=input("Enter salary: ")

file=open("employees.txt","a")
file.write(name+" "+pay+"\n")
file.close()