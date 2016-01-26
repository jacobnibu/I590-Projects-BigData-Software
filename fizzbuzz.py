def fizzbuzz(p_integer):
	for x in range(1, p_integer):
		if x%2 == 0:
			print("fizz")
		elif x%3 == 0:
			print("buzz")
		elif x%2 == 0 and x%3 == 0:
			print("fizzbuzz")
		else:
			print(x)
lv_integer = input('Enter an integer: ')
fizzbuzz(lv_integer)