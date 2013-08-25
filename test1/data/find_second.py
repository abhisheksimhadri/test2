danton = "De l'audace, encore de l'audace, toujours de l'audace"
twister = "she sells seashells on the seashore"

def find_second(search,target):
	first = search.find(target)
	second = search.find(target, first + 1)
	return second

print find_second(danton, 'audace')
print find_second(twister, 'she')

