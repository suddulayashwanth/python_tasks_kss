n=int(input("Enter number of items: "))
file=open("grocery.txt","w")
for i in range(n):
    item=input("Enter item: ")
    file.write(item+"\n")
file.close()

file=open("grocery.txt","r")
print(file.read())
file.close()