# to find greatest of three numbers
#concatination
s=int(input('enter first number=')) 
t=int(input("enter second number="))
r=int(input("enter third number="))
if s>=t and s>=r:
    print(s,"s is greatest")
elif t>=s and t>=r:
    print(t,"t is greatest")
else:
    print(r,"r pracis greatest")