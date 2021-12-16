from time import time_ns

def outer():
	x = 1
	def inner():
		nonlocal x
		print(f'x in outer function (before modifying): {x}' )
		x += 1
		print(f'x in outer function (before modifying): {x}' )
	return inner
def main():
	f = outer()
	f()

if __name__ == '__main__':
    main()