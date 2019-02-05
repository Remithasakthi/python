if Nterms <= 0:
   print("Please enter a positive integer")
elif Nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("fibonacci sequence upto",nterms,":")
   while count < Nterms:
       print(n1,end=' , ')
       nth = n1 +
       n1 = n2
       n2 = nth
       count += 1
