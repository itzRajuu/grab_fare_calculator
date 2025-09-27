# Grab Fare Calculator - Python (Input/Output Only)

def main():
    print("=== Welcome to Grab Fare Calculator ===")

    try:
        # Ask the user for inputs
        distance = float(input("Enter trip distance (in km): "))
        time = float(input("Enter trip duration (in minutes): "))

        # For now, just show the inputs back (no fare calculation yet)
        print(f"You entered: {distance} km and {time} minutes.")
        print("Fare calculation coming soon...")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()
