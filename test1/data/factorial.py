def factorial(select):
	result = 1
	while select >= 1:
		result = result*select
		select = select - 1
	return result


print factorial(40)

