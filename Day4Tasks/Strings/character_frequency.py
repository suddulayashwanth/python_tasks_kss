a=input()
d={}
for i in a:
    d[i]=d.get(i,0)+1
for i in d:
    print(i,d[i])character_frequency.py