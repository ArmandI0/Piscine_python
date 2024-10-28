import sys

def main():
	try:
		if len(sys.argv) != 3:
			raise AssertionError("AssertionError: the arguments are bad")
		entryList = sys.argv[1].split()
		length = int(sys.argv[2])
		isgreater = lambda str : len(str) > length
		newList = [str for str in  entryList if isgreater(str)]
		print(newList)
	except AssertionError as error:
		print(error)
	except ValueError as error:
		print("ValueError: the second argument must be an integer")
if __name__ == "__main__":
	main()