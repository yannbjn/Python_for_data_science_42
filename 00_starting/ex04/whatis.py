import sys

def main():
    if len(sys.argv) == 1:
        return

    try:
        assert len(sys.argv) == 2, "more than one argument is provided"
        
        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
            
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()