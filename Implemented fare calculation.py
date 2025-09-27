# Grab Fare Calculator - Python (With Calculation Function)

def calculate_fare(distance_km, time_min):
    base_fare = 3.00       # RM3 base fare
    per_km = 1.20          # RM1.20 per km
    per_minute = 0.50      # RM0.50 per minute (traffic time)

    # Fare formula
    fare = base_fare + (distance_km * per_km) + (time_min * per_minute)
    return fare

def main():
    print("=== Welcome to Grab Fare Calculator ===")

    try:
        distance = float(input("Enter trip distance (in km): "))
        time = float(input("Enter trip duration (in minutes): "))

        # Use the calculation function
        total_fare = calculate_fare(distance, time)

        print(f"Estimated Fare: RM {total_fare:.2f}")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()

