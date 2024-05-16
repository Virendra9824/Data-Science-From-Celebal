def upper_triangular(rows):
    for i in range(rows):
        for j in range(rows - i):
            print("*", end=" ")
        print()



rows = int(input("Enter the number of rows: "))

print("\nUpper Triangular Pattern:")
upper_triangular(rows)
