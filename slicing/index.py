#slicing & indexing
#String SlicingSlicing allows you to grab a specific subsection of a string. The syntax uses square brackets with up to three parameters separated by colons: string[start:end:step].start: The index where the slice begins (inclusive). Defaults to 0.end: The index where the slice stops (exclusive—it does not include this character). Defaults to the end of the string.step: The step size or increment interval. Defaults to 1. 
lt=[10,2,60,80,75,59,1]
print(lt[1:5]) #range

print(lt[:])   #whole list

print(lt[-1])  #last element using negative indexing

print(lt[-2])  #second-last element

print(lt[::2]) #selects every 2nd element starting from beginning..jumps to 2nd elements ..skipping 1 element in between

print(lt[::3])   #selects every 3nd element starting from beginning..jumps to 3nd elements ..skipping 2 element in between

print(lt[2:])  #extracts all elements from index 2 to end ...skipping first 2 elements
print(lt[1:-1]) #extracts all elements from index 1 upto the last element

print(lt[-1::])  #gives last element
print(lt[-1:])   #gives last element
