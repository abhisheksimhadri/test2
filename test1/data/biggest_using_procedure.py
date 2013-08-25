def bigger(a,b):
	if a > b:
		return a
	return b

def biggest(x,y,z):
	return bigger(bigger(x,y),z)

print biggest(123,234,345)
print biggest(2,1,3)
print biggest(9,8,7)
print biggest(5,2,3)

print max(345,645,298)
