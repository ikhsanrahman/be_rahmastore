import random
import string


def code_item_generator(size=10,  chars=string.ascii_lowercase + string.digits):
	code = []
	for _ in range(size):
		code.append(''.join(random.choices(chars)))
	code = ''.join(code)
	return code