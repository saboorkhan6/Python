#while-loop

n=0
while n<30:
    n=int(input("enter a number="))
    print(n)

while True:
    i=int(input("enter a number"))
    if i%2==0:
        print(i,'is even')
    else:
        print(i,'is odd')
    s=input("continue ?")
    if s !="yes":        
      break
