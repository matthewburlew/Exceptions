def get_valid_number(prompt, data_type):
    while True:
        try:
            value = data_type(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    units = get_valid_number("Enter units sold: ", int)
    price = get_valid_number("Enter price per unit: $", float)

    total = units * price
    print(f"\nTotal Revenue: ${total:.2f}")


if __name__ == "__main__":
    main()
