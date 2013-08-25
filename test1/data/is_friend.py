def is_friend(name):
	if name[0] == 'D':
		return True
	elif name[0] == 'd':
		return True
	else :
		return False


print is_friend('Diane')
print is_friend('Fred')

