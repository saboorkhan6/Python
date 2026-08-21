#palindrome
word=input("Enter your word:")
reverse=''
for letter in word:
    reverse=letter+reverse
if reverse==word:
        print(word,"is a palindrome")
else:
        print(word,"is not a palindrome") 