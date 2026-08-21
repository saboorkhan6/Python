x = int(input("Enter an number:-"))
if x <=1:
  print("Not prime")
else:
  for i in range(2,x):

    if x % i ==0:
      
      print("Not Prime number")
      break
            
  else:
      print("Prime number")