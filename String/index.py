#string
str1="this is a simple program"
str2=""
print(len(str2))
print(str1)
print(str1[6])
print(str1[10:16])  #In Python slicing str1[start:end], the end index is exclusive — meaning Python stops before that index, not at it.
print(str1[:4])

#homework
#string #slicing
strr="python programming"
print(len(strr))
print(strr[0])
print(len(strr)-1)
print(strr[17])
print(strr[:6])
print(strr[7:18])
. String SlicingSlicing allows you to grab a specific subsection of a string. The syntax uses square brackets with up to three parameters separated by colons: string[start:end:step].start: The index where the slice begins (inclusive). Defaults to 0.end: The index where the slice stops (exclusive—it does not include this character). Defaults to the end of the string.step: The step size or increment interval. Defaults to 1.
