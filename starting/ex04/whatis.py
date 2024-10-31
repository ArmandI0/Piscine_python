import sys

def main():
	try:
		ac = len(sys.argv)
		if ac == 1:
			return
		assert ac <= 2, "more than one argument is provided"
		try:
			av = int(sys.argv[1])
			if (av % 2) != 0:
				print("Im Odd.")
			else:
				print("I'm Even.")
		except:
			raise AssertionError("Argument is not an integer")
	except AssertionError as msg:
		print(f"{AssertionError.__name__} : {msg}")

if __name__ == "__main__":
	main()