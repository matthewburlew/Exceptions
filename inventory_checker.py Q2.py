def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    inventory = get_int("Current inventory level: ")
    threshold = get_int("Minimum reorder threshold: ")

    if inventory < threshold:
        print("Reorder alert: inventory is below the threshold.")

    try:
        percent = (inventory / threshold) * 100
        print(f"Inventory is {percent:.1f}% of the threshold.")
    except ZeroDivisionError:
        print("Cannot calculate percentage because the threshold is 0.")


if __name__ == "__main__":
    main()
           