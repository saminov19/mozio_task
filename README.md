# Mozio API Documentation

This documentation provides an overview of the Mozio API methods and their usage. The Mozio API allows you to search for transportation services, make bookings, and perform other related operations.

## Authentication

To use the Mozio API, you need to include the `API-KEY` header in your API requests. The API key can be obtained by registering on the Mozio platform.

## API Methods

### Search

The `search` method allows you to search for transportation services based on various parameters.

**Endpoint**: `/search/`
**Allowed Methods**: POST

**Parameters**:
- `start_address`: The starting address of the journey.
- `end_address`: The destination address of the journey.
- `mode`: The mode of transportation (e.g., one_way, round_trip).
- `pickup_datetime`: The date and time of the pickup.
- `num_passengers`: The number of passengers.
- `currency`: The currency for pricing.
- `campaign`: Your campaign name.

**Response**: Returns the search results containing information about available transportation options.

### Poll Search

The `poll_search` method allows you to poll the search status until a valid response is obtained.

**Endpoint**: `/search/{search_id}/poll/`
**Allowed Methods**: GET

**Parameters**:
- `search_id`: The ID of the search request.

**Response**: Returns the search status, indicating the progress and availability of search results.

### Book

The `book` method allows you to make a booking based on the selected search result.

**Endpoint**: `/reservations/`
**Allowed Methods**: POST

**Parameters**:
- `search_id`: The ID of the search request.
- `result_id`: The ID of the selected search result.
- `email`: The email address of the passenger.
- `country_code_name`: The country code name of the passenger's phone number.
- `phone_number`: The phone number of the passenger.
- `first_name`: The first name of the passenger.
- `last_name`: The last name of the passenger.
- `airline`: The airline for flight bookings (if applicable).
- `flight_number`: The flight number for flight bookings (if applicable).
- `customer_special_instructions`: Special instructions provided by the customer.

**Response**: Returns the booking status and details of the reservation.

### Poll Booking

The `poll_booking` method allows you to poll the booking status until a valid response is obtained.

**Endpoint**: `/reservations/{search_id}/poll/`
**Allowed Methods**: GET

**Parameters**:
- `search_id`: The ID of the search request.

**Response**: Returns the booking status, including the reservation ID and confirmation number.

### Cancel Booking

The `cancel_booking` method allows you to cancel a booking.

**Endpoint**: `/reservations/{booking_id}`
**Allowed Methods**: DELETE

**Parameters**:
- `booking_id`: The ID of the booking to be canceled.

**Response**: Returns the cancellation status and details of the canceled booking.

## Example Usage

```python
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

# Poll the search status until a valid response is obtained
search_status = poll_search(search_id)

# Perform the booking and further steps
booking_details = {
  "email": "happytraveler4@mozio.com",
  "country_code_name": "US",
  "phone_number": "8776645525",
  "first_name": "Happy4",
  "last_name": "Traveler4",
  "airline": "AA",
  "flight_number": "254",
  "customer_special_instructions": "My doorbell is broken, please yell"
}

result_id = search_status["results"][0]["result_id"]

# Make the booking
booking_response = book(search_id, result_id, **booking_details)

# Poll the booking status until a valid response is obtained
booking_poll = poll_booking(search_id)

# Check if the reservations key exists before accessing its value
if "reservations" in booking_poll:
    reservation_id = booking_poll["reservations"][0]["id"]
    confirmation_number = booking_poll["reservations"][0]["confirmation_number"]
    print("Reservation ID:", reservation_id)
    print("Confirmation Number:", confirmation_number)
else:
    print("No reservations found for the given search ID.")

# Cancel the booking
cancel_response = cancel_booking(reservation_id)
print("Booking Canceled:", cancel_response)
