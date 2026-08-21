n = [12,25,90,21,46,101,31]

flag = 0
x = int(input("Enter an number:-"))
for num in n :
  if x == num:
    flag =1
    
if flag ==1:
  print(x,'is in list')
else:
  print(x,"is not in list")