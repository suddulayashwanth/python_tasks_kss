file=open("marks.txt","r")
total=0
count=0

for line in file:
    print(line.strip())
    data=line.split()
    total+=int(data[1])
    count+=1

file.close()

print("Average Marks =",total/count)