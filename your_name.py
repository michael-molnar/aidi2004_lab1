# Python program to take a user's name, 
# count the number of letters, 
#and then print it backwards

name = input('Enter your name: ')
count = 0
for char in name:
	if char.isalpha():
		count +=1

print('There are {} letters in your name.'.format(count))
print('Your name backwards is: ', name[::-1])