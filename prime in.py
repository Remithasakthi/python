lower=90:
upper=900:
    print("print number between",lower,"and",upper,"are:")
    for num in range(lower,upper+1):
        if num>1:
            for i in range(2,num):
                if(num%i)==0:
                    break
                else:
                    print(number)
