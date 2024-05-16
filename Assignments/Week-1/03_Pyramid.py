def pyramid(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "* " * (i + 1))



rows = int(input("Enter the number of rows: "))

print("\nPyramid Pattern:")
pyramid(rows)


