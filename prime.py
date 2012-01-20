def find_primes(max):

	primes = list(range(3, max, 2))
	
	for i in range(3, max, 2):
		if i in primes:
			j = i
			while j < max:
				j = j + i
				if j in primes:
					primes.remove(j)
					
	return primes
	
def is_prime(num):
	
	if num <= 1:
		return False
		
	if num == 2:
		return True
	
	if num % 2 == 0:
		return False
	else:	
		divisors = range(3, int(num / 2), 2)
		for divisor in divisors:
			if num % divisor == 0:
				return False
		return True