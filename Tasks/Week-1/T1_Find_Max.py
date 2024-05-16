def find_max(num1, num2, num3):
    if(num1>num2 and num1>num3):
        return num1
    
    elif(num2>num1 and num2>num3):
        return num2
    
    else:   
        return num3





def main():
    num1 = float(input("Enter First number: "))
    num2 = float(input("Enter Second number: "))
    num3 = float(input("Enter Third number: "))

    result = find_max(num1, num2, num3)

    print("The largest number is:", result)



if __name__ == "__main__":
    main()
