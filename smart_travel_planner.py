"""A beginner-friendly console program for estimating a trip's costs."""


def calculate_transportation_cost(cost_per_traveler, travelers):
    return cost_per_traveler * travelers


def calculate_hotel_cost(cost_per_traveler_per_day, days, travelers):
    return cost_per_traveler_per_day * days * travelers


def calculate_food_cost(cost_per_traveler_per_day, days, travelers):
    return cost_per_traveler_per_day * days * travelers


def calculate_activity_cost(cost_per_traveler, travelers):
    return cost_per_traveler * travelers


def calculate_total_cost(transportation, hotel, food, activities):
    return transportation + hotel + food + activities


def calculate_cost_per_traveler(total_cost, travelers):
    return total_cost / travelers


def calculate_average_daily_cost(total_cost, days):
    return total_cost / days


def get_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value.")


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Enter a whole number greater than 0.")
        except ValueError:
            print("Enter a valid whole number.")


def get_non_negative_cost(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Cost cannot be negative.")
        except ValueError:
            print("Enter a valid number, such as 25 or 25.50.")


def main():
    print("SMART TRAVEL PLANNER")
    print("Enter trip details and estimated costs.\n")

    travel_name = get_non_empty_text("Travel name: ")
    destination = get_non_empty_text("Destination: ")
    travelers = get_positive_integer("Number of travelers: ")
    days = get_positive_integer("Number of travel days: ")

    transportation_per_traveler = get_non_negative_cost(
        "Transportation cost per traveler: $"
    )
    hotel_per_traveler_per_day = get_non_negative_cost(
        "Hotel cost per traveler, per day: $"
    )
    food_per_traveler_per_day = get_non_negative_cost(
        "Food cost per traveler, per day: $"
    )
    activities_per_traveler = get_non_negative_cost(
        "Activity cost per traveler for the trip: $"
    )

    # A dictionary keeps the related trip details together.
    trip = {
        "name": travel_name,
        "destination": destination,
        "travelers": travelers,
        "days": days,
        "transportation_per_traveler": transportation_per_traveler,
        "hotel_per_traveler_per_day": hotel_per_traveler_per_day,
        "food_per_traveler_per_day": food_per_traveler_per_day,
        "activities_per_traveler": activities_per_traveler,
    }

    transportation_total = calculate_transportation_cost(
        trip["transportation_per_traveler"], trip["travelers"]
    )
    hotel_total = calculate_hotel_cost(
        trip["hotel_per_traveler_per_day"], trip["days"], trip["travelers"]
    )
    food_total = calculate_food_cost(
        trip["food_per_traveler_per_day"], trip["days"], trip["travelers"]
    )
    activity_total = calculate_activity_cost(
        trip["activities_per_traveler"], trip["travelers"]
    )
    overall_total = calculate_total_cost(
        transportation_total, hotel_total, food_total, activity_total
    )
    per_traveler = calculate_cost_per_traveler(overall_total, trip["travelers"])
    daily_average = calculate_average_daily_cost(overall_total, trip["days"])

    print("\n" + "=" * 42)
    print("             TRAVEL SUMMARY")
    print("=" * 42)
    print(f"Travel name:                    {trip['name']}")
    print(f"Destination:                    {trip['destination']}")
    print(f"Travelers:                      {trip['travelers']}")
    print(f"Travel days:                    {trip['days']}")
    print("-" * 42)
    print(f"Total transportation cost:      ${transportation_total:,.2f}")
    print(f"Total hotel cost:               ${hotel_total:,.2f}")
    print(f"Total food cost:                ${food_total:,.2f}")
    print(f"Total activity cost:            ${activity_total:,.2f}")
    print("-" * 42)
    print(f"Overall trip cost:              ${overall_total:,.2f}")
    print(f"Cost per traveler:              ${per_traveler:,.2f}")
    print(f"Average cost per day (all):     ${daily_average:,.2f}")
    print("=" * 42)


if __name__ == "__main__":
    main()