# Define function that holds hotel cost and the number of nights the users is going to stay
# Ask user to input what their nightly hotel budget  
# Return the total cost by calculating the nighlty rate * the number of nights
def hotel_cost(num_nights):
    nightly_rate = 1200
    total_cost = nightly_rate * num_nights
    return total_cost

# Define the flight cost and which city the user is flying to
# Use a dictionary to create a list of cities and their flight prices
def plane_cost(city_flight):
    city_prices = {
        "durban": 1150,
        "johannesburg": 1200,
        "tshwane": 1250,
        "cape town": 1170,
        "mpumalanga": 1120
}
    # Use a if statement and return the city flight and price the user chose
    # Use a else statment if user chose a city not in the dictionary with apology message
    city_flight_lower = city_flight.lower()  # Convert user input to lowercase

    if city_flight_lower in city_prices:
        return city_prices[city_flight_lower]
    else:
        return 0
# Define function for vehicle rental and the amount of days it is needed for
# Ask the user to input what their daily budget for the rental is
# Return the total cost by calculating the daily rental rate * the amount of days it is needed for
def car_rental(rental_days):
    daily_rental_rate = 1000
    total_cost = daily_rental_rate * rental_days
    return total_cost

# Define function for the cost of the holiday holding the 3 parameters
# Return the total cost of the holiday by calculating and adding the 3 parameters up
def holiday_cost(hotel_cost, plane_cost, car_rental):
    hotel_total = (hotel_cost(num_nights))
    plane_total = plane_cost(city_flight)
    car_total = car_rental(rental_days)

    total_holiday_cost = hotel_total + plane_total + car_total
    return total_holiday_cost

# Use a if statement to to set the name of script as main executed code
# Ask user to enter the city they flying to
# ask user to enter the amount of nights they will be staying at the hotel
# Ask user the amount of days they need the rental vehicle for
if __name__ == "__main__":
    city_flight = input("Enter the city you will be flying to: ")
    num_nights = int(input("Enter the number of nights needed for accomodation: "))
    rental_days = int(input("Enter the number of days you will be hiring a rental car for: "))
    

    # Calculate the total holiday cost adding up the 3 parameters
    total_cost = holiday_cost(hotel_cost, plane_cost, car_rental)

    # Print the results
    print("\nHoliday Details")
    print(f"City: {city_flight}")
    print(f"Total Holiday Cost: R{total_cost}")

