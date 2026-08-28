# #file-handling: create(write) ,update (read,append) and delete a particular file


# #write
# file=open("hello.txt",'w')
# file.write("This is a file")
# file.close()

# #write-overwrite
# file=open("hello.txt","w")
# file.write("overwrittten text")
# file.close()

# #read
# file=open("hello.txt","r")
# new=file.read()
# print(new)

# #append
# file=open("hello.txt","a")
# file.write(" appended text")
# file.close()


# #delete=doesn't work
# # file=open("hello.txt","x")
# # file.close()

# #write+read+binary format
# file=open("new.txt","w+b")
# file.write(b"abccc")
# file.close()


#external file
file=open(r"C:\Users\Saboor\OneDrive\Desktop\external\file.txt","w")
file.write("hello world")
file.close()

with open ("file2.txt","w") as s:
    s.write("modern file handling")
    
#write+read+binary format
file=open("new.txt","w+b")
file.write(b"abccc")
file.close()
