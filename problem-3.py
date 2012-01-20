# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math
	
num = 600851475143
#num = 13195
orig_num = num

found = True
while found:
	#print("Finding divisors of {0}".format(num))
	
	found = False
	for divisor in range(2, int(math.sqrt(num))):
		if num % divisor == 0:
			#print("Found divisor {0}".format(divisor))
			
			found = True
			num = int(num / divisor)
			break
			
print("Biggest prime divisor of {0} is {1}".format(orig_num, num))