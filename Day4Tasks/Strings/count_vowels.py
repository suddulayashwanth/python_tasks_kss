a=input()
c=0
for i in a.lower():
    if i in "aeiou":
        c+=1
print(c)