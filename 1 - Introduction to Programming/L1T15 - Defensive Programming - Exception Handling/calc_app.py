def perform_calculation(number1, number2, operator):
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        if number2 != 0:
            result = number1 / number2
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operator!"

    equation = f"{number1} {operator} {number2} = {result}"
    record_equation(equation)
    return equation


def record_equation(equation):
    with open("equations.txt", "a") as file:
        file.write(equation + "\n")


def print_previous_equations():

    
    try:
        with open("equations.txt", "r") as file:
            equations = file.readlines()
            for equation in equations:
                print(equation.strip())
    except FileNotFoundError:
        print("No previous equations found.")


def main():
    print("Welcome to the Calculator App!")

    while True:
        print("\nMenu:")
        print("1. Use Calculator")
        print("2. Previous Calculations")
        print("3. Exit")

        choice = input("Please select an option: ")

        if choice == "1":
            try:
                number1 = float(input("Enter the first number: "))
                number2 = float(input("Enter the second number: "))
                operator = input("Enter the operator (+, -, *, /): ")

                result = perform_calculation(number1, number2, operator)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        elif choice == "2":
            print_previous_equations()
        elif choice == "3":
            print("Exiting the calculator.....Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
