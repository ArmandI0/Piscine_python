import sys

NESTED_MORSE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
	' ': '/'
}

def main():
	try:
		if len(sys.argv) != 2:
			raise AssertionError("AssertionError: the arguments are bad")
		str = sys.argv[1]
		if not all(char.isalnum() or char.isspace() for char in str):
			raise AssertionError("AssertionError: the arguments are bad")
		for char in str:
			print(NESTED_MORSE[char.upper()], end=" ")
		print()
	except AssertionError as error:
		print(error)

if __name__ == "__main__":
	main()