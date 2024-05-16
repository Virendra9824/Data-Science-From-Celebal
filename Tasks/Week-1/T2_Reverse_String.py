def reverseString(str):
    n = len(str)
    ans = ""
    for i in range(0, n):
        print(n-i-1)
        ans += str[n-i-1]

    return ans



def main():
    str = input("Enter a String: ", )

    result = reverseString(str)
    print("Reverse of ",str, " is:", result)




if __name__ == "__main__":
    main()