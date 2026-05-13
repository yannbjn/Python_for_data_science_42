import sys


def count_chars(text: str):
    """
    Counts and prints the number of uppercase, lowercase, punctuation,
    digits, and space characters in a given string.
    """
    upper_count = 0
    lower_count = 0
    punct_count = 0
    space_count = 0
    digit_count = 0

    # Hardcoding standard ASCII punctuation to avoid importing the string module,
    # adhering strictly to the allowed libraries constraint.
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1
        elif char in punctuation:
            punct_count += 1

    total = len(text)
    print(f"The text contains {total} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punct_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    """
    Main function that parses the argument, reads from stdin if necessary,
    handles AssertionErrors, and displays character counts.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        if len(sys.argv) == 1 or sys.argv[1] is None:
            print("What is the text to count?")
            # text = sys.stdin.read() 
            text = sys.stdin.readline()
        else:
            text = sys.argv[1]

        count_chars(text)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()