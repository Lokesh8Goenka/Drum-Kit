#Q2
def fibonacci(n):
	if (n == 0):
		return 0
	elif (n == 1 or n == 2):
		return 1
	else:
            f = fibonacci(n-1) + fibonacci(n-2)
            print(f)
            return f

print(fibonacci(10))