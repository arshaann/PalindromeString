name = input("Enter a name: ")
temp = ""


for i in name:
	temp+=i

if temp == name:
	print("Name is a palindrome")
else:
	print("Name is not a palindrome")


