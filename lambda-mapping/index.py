#lambda : for smaller tasks using keyword - lambda
#add using lambda :
add=lambda x,y: x+y
print(add(1,2))

#even-odd using lambda
even_odd=lambda x:"even" if x%2==0 else "odd"
print(even_odd(4))

#map: iterates from one variable to another {lambda is like smaller version of function and map is like for loop a sit does the iteration part}

#to find square of all elements in the list
lt=[1,2,3,4,5]
sqr=list(map(lambda i: i*i,lt))
print(sqr)

#type-changing using map
new=['1','2','3','4']
a=list(map(int,new))   
print(a)