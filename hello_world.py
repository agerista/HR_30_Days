# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
inputString = raw_input()

# Print a string literal saying "Hello, World." to stdout.
print 'Hello, World.'

# TODO: Write a line of code here that prints the contents of input_string to stdout.
print inputString

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nAll tests passed. Good job!\n"
