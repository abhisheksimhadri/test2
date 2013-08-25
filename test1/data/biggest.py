def biggest(a,b,c):
	if a > b:
		if a > c:
			return a
		else:
			return c
	else:
		if b > c:
			return b
		else:
			return c

print biggest(213,245,89)
print biggest(3,1,4)
print biggest(5,6,7)
