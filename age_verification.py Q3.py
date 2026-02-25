def get_customer_age():
    while True:
        try:
            age = int(input("Enter customer age: "))
            if age <= 0:
                raise ValueError
            return age
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def main():
    try:
        age = get_customer_age()

        if age >= 18:
            print("Customer is eligible for the promotion.")
        else:
            print("Customer is NOT eligible for the promotion.")

    except NameError:
        print("An unexpected NameError occurred.")


if __name__ == "__main__":
    main()
