def read_and_sum_numbers(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = []
            for line in file:
                for word in line.split():
                    if word.isdigit():  
                        numbers.append(int(word))
                        
            total_sum = sum(numbers)

            print(f"Numbers in the file: {numbers}")
            print(f"Sum of the numbers: {total_sum}")
            return total_sum
    
    except Exception as e:
        print(f"An error occurred: {e}")





# Writing data into file
file = open('file2.txt', 'wt')
file.write("The numbers are: 1 2 3 4 5 6 7 8 9 10")
file.close()



file_path = './file2.txt'  
read_and_sum_numbers(file_path)
