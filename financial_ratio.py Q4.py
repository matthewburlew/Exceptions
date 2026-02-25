def main():
    while True:
        try:
            profit = float(input("Enter profit: "))
            revenue = float(input("Enter revenue: "))

            ratio = profit / revenue  # May raise ZeroDivisionError

        except ValueError:
            print("Invalid input. Please enter numeric values.")
            pass

        except ZeroDivisionError:
            print("Revenue cannot be zero.")
            pass

        else:
            percentage = ratio * 100
            print(f"Profit Margin: {percentage:.2f}%")
            break


if __name__ == "__main__":
    main()
