def ispangram(str):
	a = "abcdefghijklmnopqrstuvwxyz"
	for char in a:
		if char not in str.lower():
			return False
	return True
string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string) == True):
	print("Yes")
else:
	print("No")
string = 'hi im attending python zero to hero camp'
if(ispangram(string) == True):
	print("Yes")
else:
	print("No")
