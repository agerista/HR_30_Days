i = 4
d = 4.0
s = "Hacker Rank"

# Declare second integer, double, and String variables.

# Read and save an integer, double, and String to your variables.
i2 = int(raw_input())
d2 = float(raw_input())
s2 = str(raw_input())
# Print the sum of both integer variables on a new line.
print i + i2
# Print the sum of the double variables on a new line.
print d + d2
# Concatenate and print the String variables on a new line
print s + s2
# The 's' variable above should be printed first.

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nAll tests passed. Good job!\n"
