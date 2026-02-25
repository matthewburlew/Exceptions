def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a valid number.")


def main():
    while True:
        try:
            salary = get_number("Enter current salary: $")
            pct = get_number("Enter adjustment percentage (0-100): ")

            if salary < 0:
                raise ValueError("Salary cannot be negative.")

            if not (0 <= pct <= 100):
                raise ValueError("Percentage must be between 0 and 100.")

            new_salary = salary * (1 + pct / 100)
            print(f"New salary: ${new_salary:.2f}")
            break

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
