def abbaize(x,y):
	string1 = str(x)
	string2 = str(y)
	output = string1 + string2 + string2 + string1
	return output

print abbaize('a','b')
print abbaize('dog','cat')
