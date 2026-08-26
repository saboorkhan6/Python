#filter:
#evem-odd using filter
num=[1,2,3,4,5,6,7,8]
a=list(filter(lambda x:x%2==0,num))
print(a)

#negative-positive using filter
new=[-1,2,-3,4,-5,-6,-7]
s=list(filter(lambda x:x<0,new))
print(s)


colours=["red","blue","green","yellow"]
n=list(filter(lambda i:len(i)>3,colours))
print(n)