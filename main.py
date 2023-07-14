import json
from datetime import datetime
import time


# Import the implemented API methods
from api_methods import search, poll_search, book, poll_booking, cancel_booking


# Perform the search
start_address = "44 Tehama Street, San Francisco, CA, USA"
end_address = "SFO"
mode = "one_way"
pickup_datetime = "2023-12-01T15:30:00-08:00"
num_passengers = 2
currency = "USD"
campaign = "Your Full Name"

search_response = search(start_address, end_address, mode, pickup_datetime, num_passengers, currency, campaign)
search_id = search_response["search_id"]
print("Search ID: " + search_id)
print("Search response: ")
print(search_response)




# Poll the search status until a valid response is obtained
search_status = poll_search(search_id)
print("Search status:")
print(search_status)




def find_cheapest_vehicle(json_data):
    data = json.loads(json_data)
    results = data.get("results", [])

    cheapest_result = None
    for result in results:
        provider_name = result["steps"][0]["details"]["provider"]["name"]
        if provider_name == "Dummy External Provider":
            price_value = float(result["total_price"]["total_price"]["value"])

            if cheapest_result is None or price_value < float(cheapest_result["total_price"]["total_price"]["value"]):
                cheapest_result = result
    
    return cheapest_result

# Convert the JSON data to a string
json_str = json.dumps(search_status)
cheapest_result = find_cheapest_vehicle(json_str)
print("Cheapest result:")
print(cheapest_result)







# Perform the booking and further steps
booking_details = {
  "email": "happytraveler4@mozio.com",
  "country_code_name": "US",
  "phone_number": "8776645525",
  "first_name": "Happy4",
  "last_name": "Traveler4",
  "airline": "AA",
  "flight_number": "254",
  "customer_special_instructions": "My doorbbell is brokennn, pleasee yell"
}


result_id = cheapest_result["result_id"]

# Make the booking
booking_response = book(search_id, result_id, **booking_details)
print(booking_response)

time.sleep(100)

booking_poll = poll_booking(search_id)

if "reservations" in booking_poll:
    reservation_id = booking_poll["reservations"][0]["id"]
    confirmation_number = booking_poll["reservations"][0]["confirmation_number"]
    print(f"Reservation ID: {reservation_id}")
    print(f"Confirmation Number: {confirmation_number}")
else:
    print("No reservations found for the given search ID.")
    
    
# reservation_id = booking_poll["reservations"][0]["id"]
# confirmation_number = booking_poll["reservations"][0]["confirmation_number"]

print("Booking Successful!")
print("Confirmation Number:", confirmation_number)




# Cancel the booking
cancel_response = cancel_booking(reservation_id)
print("Booking Canceled:")
print(cancel_response)