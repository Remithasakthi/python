lower=int(input("Enter a number:"))
upper=int(input("Enter a number:"))
for num in range(lower,upper+1):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if num==sum:
        print(num)
    
