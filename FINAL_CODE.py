# Grab Fare Calculator 
def calculate_fare(distance_km, time_min, base, per_km, per_min):
    # Fare formula
    fare = base + (distance_km * per_km) + (time_min * per_min)
    return fare

def main():
    print("=== Welcome to Grab Fare Calculator ===")

    # Step 1: Choose ride type
    print("\nChoose ride type:")
    print("1. GrabCar  (Base: RM3,  RM1.20/km, RM0.50/min)")
    print("2. GrabBike (Base: RM2,  RM0.80/km, RM0.30/min)")
    print("3. GrabPremium (Base: RM5, RM2.00/km, RM0.80/min)")

    try:
        choice = int(input("Enter choice (1-3): "))

        if choice == 1:
            ride_type, base, per_km, per_min = "GrabCar", 3.0, 1.2, 0.5
        elif choice == 2:
            ride_type, base, per_km, per_min = "GrabBike", 2.0, 0.8, 0.3
        elif choice == 3:
            ride_type, base, per_km, per_min = "GrabPremium", 5.0, 2.0, 0.8
        else:
            print("Invalid choice! Defaulting to GrabCar.")
            ride_type, base, per_km, per_min = "GrabCar", 3.0, 1.2, 0.5

        # Step 2: Get user trip details
        distance = float(input("\nEnter trip distance (in km): "))
        time = float(input("Enter trip duration (in minutes): "))

        # Step 3: Calculate fare
        total_fare = calculate_fare(distance, time, base, per_km, per_min)

        # Step 4: Promo code
        promo = input("\nEnter promo code (if any): ").upper()
        if promo == "GRAB10":
            discount = total_fare * 0.10
            total_fare *= 0.90
            print(f"Promo applied: GRAB10 (10% off, saved RM {discount:.2f})")
        elif promo == "GRAB20":
            discount = total_fare * 0.20
            total_fare *= 0.80
            print(f"Promo applied: GRAB20 (20% off, saved RM {discount:.2f})")
        elif promo.strip() == "":
            print("No promo code entered.")
        else:
            print("Invalid promo code! No discount applied.")

        # Step 5: Display result
        print("\n==== Grab E-Receipt ====")
        print(f"Ride Type : {ride_type}")
        print(f"Distance  : {distance} km")
        print(f"Time      : {time} minutes")
        print(f"Total Fare: RM {total_fare:.2f}")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()
