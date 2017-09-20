a = input("Enter the text: ")
b = (a[::-1])
if list(a) == list(b):
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")
