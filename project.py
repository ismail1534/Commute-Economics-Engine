import csv
import sys
import requests


class Vehicle:
    def __init__(self, name, efficiency):
        self.name = name
        self.efficiency = float(efficiency) 

class Commute:
    def __init__(self, vehicle, daily_km, fuel_price):
        self.vehicle = vehicle
        self.daily_km = float(daily_km)
        self.fuel_price = float(fuel_price)

    def daily_cost(self):
        return calculate_daily_cost(self.daily_km, self.vehicle.efficiency, self.fuel_price)


def load_vehicles(filename):
    
    vehicles = []
    try:
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                vehicles.append(Vehicle(row["name"], row["efficiency_kmpl"]))
    except FileNotFoundError:
        sys.exit(f"Error: '{filename}' not found. Make sure vehicles.csv is in the same folder.")
    return vehicles


def get_fuel_price():
   
    FALLBACK_PRICE = 262.0 

    try:
        response = requests.get("https://open.er-api.com/v6/latest/USD", timeout=5)
        data = response.json()

        if data.get("result") == "success":
            usd_to_pkr = data["rates"]["PKR"]
            estimated = round(0.70 * usd_to_pkr, 2)
            print(f"  (Live rate: 1 USD = Rs. {usd_to_pkr})")
            return estimated

    except Exception:
        pass

    print("  (Could not reach API. Using default price.)")
    return FALLBACK_PRICE


def calculate_daily_cost(daily_km, efficiency, fuel_price):
    
    liters_used = daily_km / efficiency
    return round(liters_used * fuel_price, 2)


def calculate_costs(daily_cost):
  
    return {
        "daily":   round(daily_cost, 2),
        "weekly":  round(daily_cost * 5,   2),
        "monthly": round(daily_cost * 22,  2),
        "yearly":  round(daily_cost * 264, 2),
    }


def main():
    print("\n" + "=" * 52)
    print("       COMMUTE ECONOMICS ENGINE — Pakistan")
    print("=" * 52)

    vehicles = load_vehicles("vehicles.csv")

    print("\nAvailable Vehicles:")
    for i, v in enumerate(vehicles, 1):
        print(f"  {i}. {v.name}  ({v.efficiency} km/L)")

    while True:
        try:
            choice = int(input("\nSelect your vehicle (enter number): ")) - 1
            if 0 <= choice < len(vehicles):
                selected = vehicles[choice]
                break
            print(f"  Enter a number between 1 and {len(vehicles)}.")
        except ValueError:
            print("  Please enter a valid number.")

    while True:
        try:
            daily_km = float(input("Daily commute distance in km (both ways): "))
            if daily_km > 0:
                break
            print("  Distance must be greater than 0.")
        except ValueError:
            print("  Please enter a valid number.")

    print("\nFetching current fuel price...")
    fuel_price = get_fuel_price()
    print(f"  Estimated price: Rs. {fuel_price}/liter")
    print("  Tip: Override below with the exact OGRA price for best accuracy.\n")

    override = input("Enter a custom fuel price? (y/n): ").strip().lower()
    if override == "y":
        while True:
            try:
                fuel_price = float(input("  Petrol price (Rs./liter): "))
                if fuel_price > 0:
                    break
                print("  Price must be greater than 0.")
            except ValueError:
                print("  Please enter a valid number.")

    commute = Commute(selected, daily_km, fuel_price)
    daily = commute.daily_cost()
    costs = calculate_costs(daily)

    print("\n" + "=" * 52)
    print(f"  COST REPORT  —  {selected.name}")
    print("=" * 52)
    print(f"  Daily Distance   : {daily_km} km")
    print(f"  Fuel Price       : Rs. {fuel_price}/liter")
    print(f"  Fuel Efficiency  : {selected.efficiency} km/L")
    print("-" * 52)
    print(f"  Daily Cost       : Rs. {costs['daily']}")
    print(f"  Weekly Cost      : Rs. {costs['weekly']}   (5 days)")
    print(f"  Monthly Cost     : Rs. {costs['monthly']}  (22 days)")
    print(f"  Yearly Cost      : Rs. {costs['yearly']}  (264 days)")
    print("=" * 52)

    print(f"\n  ALL VEHICLES  —  {daily_km} km/day @ Rs. {fuel_price}/liter")
    print("=" * 52)
    print(f"  {'Vehicle':<23}  {'Monthly':>9}  {'Yearly':>10}")
    print("-" * 52)

    for v in vehicles:
        d = calculate_daily_cost(daily_km, v.efficiency, fuel_price)
        c = calculate_costs(d)
        marker = " ◄ your pick" if v.name == selected.name else ""
        print(f"  {v.name:<23}  Rs.{c['monthly']:>6}  Rs.{c['yearly']:>9}{marker}")

    print("=" * 52 + "\n")


if __name__ == "__main__":
    main()
