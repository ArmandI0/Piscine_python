import sys
import string


def main(str: str):
    upper, lower, punctuations, lower, spaces, digits = 0
    for c in str:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c in string.punctuation:
            punctuations += 1
        elif c.isspace():
            spaces += 1
        elif c.isdigit():
            digits += 1

if __name__ == "__main__":
    
    main()