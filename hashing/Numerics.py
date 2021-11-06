

def b2tob10(a: str) -> int:

	base = 0
	num = 0
	for i in a[::-1]:
		if int(i) != 0:
			num += 2**base
			base += 1
		else:
			base += 1
	return num

def b10tob2(a: int) -> str:
	binary = ""
	remainder = 0
	while a != 0:
		remainder = a%2
		binary += str(remainder)
		a //=2
	return binary[::-1]

print(b2tob10(str(100100001000)))#2312