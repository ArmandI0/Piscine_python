import sys

punctuation = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
    '}', '~'
]


def readStdin():
    """
    Reads all lines from (stdin) and returns them as a single string.

    Returns:
        str: A single string containing all the lines read from stdin.
    """
    buffer = ""
    for line in sys.stdin.readlines():
        buffer += line
    return buffer


def main(str):
    upper, lower, punctuations, lower, spaces, digits = 0, 0, 0, 0, 0, 0
    for c in str:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c in punctuation:
            punctuations += 1
        elif c.isspace():
            spaces += 1
        elif c.isdigit():
            digits += 1
    print(f"Le texte contient {len(str)} caractères :")
    print(f"- {upper} lettres majuscules")
    print(f"- {lower} lettres minuscules")
    print(f"- {punctuations} caractères de ponctuation")
    print(f"- {spaces} espaces")
    print(f"- {digits} chiffres")


if __name__ == "__main__":
    try:
        ac = len(sys.argv)
        assert ac <= 2, "more than one argument is provided"
        if (ac == 1):
            str = readStdin()
        else:
            str = sys.argv[1]
        main(str)
    except AssertionError as error:
        print(error)
