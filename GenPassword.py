#Python Code Generation

import random
import workwithfiles as wwf

def gen():
	'''         GENERATING...
	'''
	print(gen.__doc__)
	chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	for n in range(1):
		password =''
	for i in range(10):
		password += random.choice(chars)
	print(password)

gen()


