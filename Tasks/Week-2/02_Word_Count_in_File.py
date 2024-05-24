def countWord(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            words = data.split()
            num_words = len(words)
            print(f"Number of words in given file is: {num_words}")
            return num_words
    
    except Exception as e:
        print(f"An error occurred: {e}")




# Writing data into file
file = open('file1.txt', 'wt')
file.write("Hello this is content of file1.")
file.close()


#Counting words
file_path = "./file1.txt"
countWord(file_path)




