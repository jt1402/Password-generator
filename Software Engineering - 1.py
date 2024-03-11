def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform addition
    result = num1 + num2
    print("The sum is:", result)

    # Check conditions
    if result < 0:
        print("No negative numbers allowed.")
    elif result % 5 == 0:
        print("The sum is a multiple of 5.")
    elif result % 2 == 0:
        print("The sum is an even number.")
    else:
        print("The sum is not particularly special.")    
main()
