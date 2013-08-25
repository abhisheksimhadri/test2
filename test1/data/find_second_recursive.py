danton = "De l'audace, encore de l'audace, toujours de l'audace"
twister = "she sells seashells on the seashore"

def find_second(search,target):
	return search.find(target, search.find(target) + 1)

print find_second(danton, 'audace')
print find_second(twister, 'she')

