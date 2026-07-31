num=int(input())
temp=num
sum=0
while temp>0:
    digit=temp%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    sum=sum+fact
    temp=temp//10
if sum==num:
    print("Strong Number")
else:
    print("Not Strong Number")