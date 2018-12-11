def char_ frequency(str1):
    dict={}
    for n in str1:
        keys=dict.keys()
        if n in keys:
            dict[n]+=str1
        else:
            dict[n]=str1
    return dict
print (char.frequency('google.com'))   
