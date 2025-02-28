def calculate_bill():
    # Ask the user to enter the charge for the food
    food_charge = float(input("Enter the charge for the food: $"))

    # Calculate tip (18%)
    tip_amount = food_charge * 0.18

    # Calculate sales tax (7%)
    sales_tax = food_charge * 0.07

    # Calculate total price
    total_price = food_charge + tip_amount + sales_tax

    # Display all amounts
    print("\nBill Details:")
    print(f"Food charge: ${food_charge:.2f}")
    print(f"Tip amount (18%): ${tip_amount:.2f}")
    print(f"Sales tax (7%): ${sales_tax:.2f}")
    print(f"Total price: ${total_price:.2f}")


# Run the program
if __name__ == "__main__":
    calculate_bill()