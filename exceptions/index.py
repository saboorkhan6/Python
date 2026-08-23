#exceptions:

#zero-division error
try:
    x=2/0
except ZeroDivisionError:
    print("cannot divide by zero")

#value error
try:
   num = int(input("Enter an number:-"))
   print(num)
except ValueError:
   print("Invalid value")

#type error
try:
    s="7"+2
except TypeError:
    print("type mismatch error")


 #name error
try:
  print(a)
except NameError:
  print('a is not defined')



#index error

try:
    lt=[10,22,54,7]
    print(lt[8])
except IndexError:
    print("item is not in the index")


#key error       
try:
    dt={
    "pincode":"1111"
    } 
    print(dt["name"])
except KeyError:
    print("key not available")

#attribute error
try:
    a=10
    a.append=20
except AttributeError:
    print("attribute error-attribute doesn't belong to this")

        