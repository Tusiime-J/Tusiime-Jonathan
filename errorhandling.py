def divide_numbers():
    """
    Continuously prompts the user for two numbers and performs division,
    handling potential errors (ValueError and ZeroDivisionError).
    """
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 / num2
            print(f"Result of {num1} / {num2} is: {result}")
            break 
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except ZeroDivisionError:
            print("Cannot divide by zero. Please enter a non-zero second number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    divide_numbers()
