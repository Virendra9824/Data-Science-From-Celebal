def lower_triangular(rows):
    for i in range(rows):
        for j in range(i + 1):
            print("*", end=" ")
        print()


rows = int(input("Enter the number of rows: "))

print("\nLower Triangular Pattern:")
lower_triangular(rows)