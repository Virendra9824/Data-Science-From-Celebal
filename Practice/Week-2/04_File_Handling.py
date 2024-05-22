print("\n#################################################\n")
f = open("file1.txt", "wt")
f.write("Hello, This is First Line")
f.close()


print("\n###-DELETING A FILE-###\n")
import os
os.remove("file1.txt")


print("\n###-WRITING INTO FILE-###\n")
f = open("04_1file.txt", "wt")
f.write("Hello, I am creating new File")
f.close()


print("\n###-APPENDING INTO FILE-###\n")
f = open("04_1file.txt", "at")
f.write("\nThis is second line\n")
f.write("This is third line")
f.close()


print("\n###-READING A FILE-###\n")
f = open("04_1file.txt", "rt")
for line in f:
    print(line)
    print("\n")








