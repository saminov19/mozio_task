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
  "email": "happytraveler7@mozio.com",
  "country_code_name": "US",
  "phone_number": "8770645525",
  "first_name": "Happy7",
  "last_name": "Traveler7",
  "airline": "AA",
  "flight_number": "774",
  "customer_special_instructions": "My doorbell is broken, pleaseee yeeell"
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




### Example output from the terminal
### it begins from the part where the cheapest option is found
Cheapest result:
{'result_id': '966c4ee7ec631fb4c6416b28609edae8', 'vehicle_id': '467e2e37800cc144cef852d6118e0f52', 'total_price': {'total_price': {'value': '60.00', 'display': '$60.00', 'compact': '$60'}, 'total_price_without_platform_fee': None, 'platform_fee': None, 'total_price_without_partner_fee': None, 'partner_fee': None, 'slashed_price': None}, 'tags': [], 'steps': [{'main': True, 'step_type': 'bus', 'details': {'description': '', 'vehicle': {'image': 'https://static.mozio.com/vehicles/bus_default.jpg', 'vehicle_type': {'key': 21, 'name': 'Bus'}, 'max_bags': 1, 'is_max_bags_per_person': True, 'max_passengers': 15, 'category': {'id': 1, 'name': 'Shared'}, 'num_vehicles': 1, 'total_bags': 1, 'model': None, 'make': None, 'vehicle_class': 4, 'vehicle_class_detail': {'display_name': 'Standard', 'vehicle_class_id': 4}}, 'maximum_pickup_time_buffer': 30, 'time': 25, 'provider': {'name': 'Dummy External Provider', 'display_name': 'Dummy External Provider', 'logo_url': 'https://static.mozio.com/providers/logos/defaults/blackcar_logo.png', 'rating': 5, 'rating_count': 0, 'rating_with_decimals': '5.0', 'supplier_score': None}, 'provider_name': 'Dummy External Provider', 'price': {'price': {'value': '60.00', 'display': '$60.00', 'compact': '$60'}, 'tolls_included': True, 'gratuity_included': False, 'gratuity_accepted': True}, 'departure_datetime': '2023-12-01T15:30:00-08:00', 'cancellation': {'cancellable_online': True, 'cancellable_offline': True, 'amendable': True, 'policy': [{'notice': 4, 'refund_percent': 100}]}, 'wait_time': {'minutes_included': 30, 'waiting_minute_price': None}, 'amenities': [{'key': 'wifi', 'name': 'WiFi', 'description': 'Connect to wireless internet in your car.', 'image_url': 'https://static.mozio.com/amenities/wifi.svg', 'png_image_url': 'https://static.mozio.com/amenities/wifi.png', 'input_type': 'boolean', 'included': False, 'selected': False, 'price': {'value': '10.00', 'display': '$10.00', 'compact': '$10'}}, {'key': 'wheelchair', 'name': 'Wheelchair accessible', 'description': 'This vehicle provides a ramp or lift to accommodate passengers in wheelchairs.', 'image_url': 'https://static.mozio.com/amenities/wheelchair.svg', 'png_image_url': 'https://static.mozio.com/amenities/wheelchair.png', 'input_type': 'boolean', 'included': False, 'selected': False, 'price': {'value': '15.00', 'display': '$15.00', 'compact': '$15'}}, {'key': 'english', 'name': 'English speaking driver', 'description': 'The driver will speak English, in addition to the local language.', 'image_url': 'https://static.mozio.com/amenities/english.svg', 'png_image_url': 'https://static.mozio.com/amenities/english.png', 'input_type': 'boolean', 'included': True, 'selected': False, 'price': {'value': '0.00', 'display': '$0.00', 'compact': '$0.00'}}, {'key': 'power', 'name': 'In-seat power', 'description': 'Charge devices while you travel.', 'image_url': 'https://static.mozio.com/amenities/power.svg', 'png_image_url': 'https://static.mozio.com/amenities/power.png', 'input_type': 'boolean', 'included': True, 'selected': False, 'price': {'value': '0.00', 'display': '$0.00', 'compact': '$0.00'}}, {'key': 'ride_tracking', 'name': 'Ride tracking', 'description': 'Monitor the location of your vehicle in real-time.', 'image_url': 'https://static.mozio.com/amenities/tracking.svg', 'png_image_url': 'https://static.mozio.com/amenities/tracking.png', 'input_type': 'boolean', 'included': True, 'selected': False, 'price': {'value': '0.00', 'display': '$0.00', 'compact': '$0.00'}}, {'key': 'restroom', 'name': 'Onboard restroom', 'description': 'Bathrooms are available in the vehicle.', 'image_url': 'https://static.mozio.com/amenities/restrooms.svg', 'png_image_url': 'https://static.mozio.com/amenities/restrooms.png', 'input_type': 'boolean', 'included': True, 'selected': False, 'price': {'value': '0.00', 'display': '$0.00', 'compact': '$0.00'}}], 'ticket_types': [], 'alternative_times': {'default_index': 0, 'options': [{'departure_datetime': '2023-12-01T15:30:00-08:00', 'arrival_datetime': '2023-12-01T15:49:32-08:00'}]}, 'flight_info_required': True, 'extra_pax_required': False, 'notes': '', 'terms_url': '', 'are_terms_internal': False, 'bookable': True, 'start_address_incomplete': False, 'end_address_incomplete': False, 'is_cached': False, 'hide_options': False, 'special_instructions_placeholder': '', 'service_instructions': {}, 'hourly_details': {'original_requested': 0, 'hours_requested': 0, 'minimum': 1, 'included_kilometers_per_hour': 20, 'total_included_kilometers': 0}}}], 'loyalty': None, 'supports': {'snapping': False, 'tracking': True, 'coupon': True, 'vehicle_and_driver': True, 'buffer_time': False}, 'flt_support': False, 'good_to_know_info': '* You will receive comprehensive pickup instructions in your confirmation email\n* You can make changes or cancel your ride at any time up to 4 hours before your scheduled pickup\n* Our Customer Support team is available 24/7 to assist you with any queries or concerns'}
{'status': 'pending', 'reservations': []}
{"status":"completed","reservations":[{"url":"https://api-testing.mozio.com/v2/reservations/ef43cc6b912441afb64c33f3c42cd137/","id":"ef43cc6b912441afb64c33f3c42cd137","amount_paid":"$60.00","gratuity":"$0.00","pickup_instructions":"Dummy pickup instructions","mobile_pickup_instructions":null,"confirmation_number":"DUM88412283","service_instructions":{},"ticket_url":"","voyage":{"flight_datetime":"2023-12-01T18:20:00-08:00","departure_datetime":"2023-12-01T15:30:00-08:00","arrival_datetime":"2023-12-01T15:49:32-08:00","alternative_times":["12-01-2023 15:30 -0800"],"alternative_time_index":0,"num_passengers":2,"service_type":1,"meet_and_greet_chosen":false,"currency":"USD","booking_details":{"bookable":1,"start_address_incomplete":false,"end_address_incomplete":false,"is_cached":0,"amendable":1,"cancellable_offline":1,"cancellable_online":1,"cancellation_policy":[{"notice":4,"refund_percent":100}],"gratuity_included":0,"tolls_included":1,"accepts_gratuity":1,"meet_and_greet_available":0,"meet_and_greet_default":0,"meet_and_greet_price":"$0.00","meet_and_greet_raw_price":"0","time_is_estimate":0,"wait_time":30,"waiting_minute_price":null,"terms_url":"","are_terms_internal":false,"notes":"","ignore_flight_info":0,"extra_pax_required":false,"has_vehicle_tracking":true,"has_vehicle_information":true,"cancellable_by_system":false,"provider_pays_cc_fees":false,"hide_options":0,"extra_trip_offer_data":{"extra_trip_search_link":"https://www.mozio.com/en-us/?utm_source=btp&utm_medium=btp&utm_campaign=Extra+Trip+Upsell&campaign=OneWayUpsell&num_passengers=2&start_address=PHL&pickup_datetime=12%2F01%2F2023+02%3A30+PM&coupon_code=XTRIP_XAUIO","extra_trip_iata_code":"PHL","trip_direction":"from","extra_trip_coupon_percentage":10,"extra_trip_coupon_code":"XTRIP_XAUIO"}},"start_location":{"full_address":"44 Tehama Street, San Francisco, CA, USA","formatted_address":"44 Tehama St, San Francisco, CA 94105, USA","lat":37.7876372,"lng":-122.3967284,"custom_name":"","name":"","timezone":"America/Los_Angeles","iata_code":"","icao_code":"","uic_code":"","metrolinx_code":"","rail_iata_code":"","place_id":"ChIJP4VfvHyAhYAR2Qmk3SkQLd0","state":"CA","country":"US","zipcode":"94105","is_cruise_port":false,"is_train_station":false,"is_transit_station":false,"street_number":"44","route":"Tehama St","neighborhood":"SoMa","sublocality":"","city":"San Francisco","county":"San Francisco County","google_hotel":false,"google_establishment":true,"source":5,"lang":"en-us","favorite_id":null,"favorite_source":null,"google_result":{"geometry":{"location":{"lat":37.7876372,"lng":-122.3967284},"location_type":"ROOFTOP"},"place_id":"ChIJP4VfvHyAhYAR2Qmk3SkQLd0","address_components":[{"long_name":"44","short_name":"44","types":["street_number"]},{"long_name":"Tehama Street","short_name":"Tehama St","types":["route"]},{"long_name":"SoMa","short_name":"SoMa","types":["neighborhood","political"]},{"long_name":"San Francisco","short_name":"SF","types":["locality","political"]},{"long_name":"San Francisco County","short_name":"San Francisco County","types":["administrative_area_level_2","political"]},{"long_name":"California","short_name":"CA","types":["administrative_area_level_1","political"]},{"long_name":"United States","short_name":"US","types":["country","political"]},{"long_name":"94105","short_name":"94105","types":["postal_code"]}],"formatted_address":"44 Tehama St, San Francisco, CA 94105, USA","short_name":"44 Tehama Street","types":["premise"]}},"end_location":{"full_address":"San Francisco International Airport","formatted_address":"San Francisco International Airport","lat":37.619105,"lng":-122.375237,"custom_name":"","name":"","timezone":"America/Los_Angeles","iata_code":"SFO","icao_code":"KSFO","uic_code":"","metrolinx_code":"","rail_iata_code":"","place_id":"","state":"CA","country":"US","zipcode":"94128","is_cruise_port":false,"is_train_station":false,"is_transit_station":false,"street_number":"","route":"","neighborhood":"","sublocality":"","city":"San Francisco","county":"","google_hotel":false,"google_establishment":false,"source":1,"lang":"en-us","favorite_id":null,"favorite_source":null,"google_result":null},"vehicle":{"type":"Bus","max_passengers":15,"max_bags":1,"is_max_bags_per_person":true,"image_url":"https://static.mozio.com/vehicles/bus_default.jpg","category":"bus","key":21,"num_vehicles":1,"make":null,"model":null,"vehicle_class":4,"vehicle_class_detail":{"vehicle_class_id":4,"display_name":"Standard"},"total_bags":1},"provider_currency":"USD","provider_phone":"","provider_email":"","provider_name":"Dummy External Provider","start_difference":0.0,"end_difference":0.0,"steps":[{"main":true,"step_type":"bus","details":{"description":"","time":25,"departure_datetime":"2023-12-01T15:30:00-08:00","notes":"","provider":{"id":1688,"uid":"749fe9b8-a492-4a3f-b7fc-4fa15b046409","name":"Dummy External Provider","is_active":true,"url":null,"report_currency":"USD","email":"info@mozio.com","phone_number":"+3903827802737","logo_url":"https://static.mozio.com/providers/logos/defaults/blackcar_logo.png","rating":5,"options":{"twentyfour_hour_time":false},"description":null,"has_terms":false,"rating_count":0,"rating_with_decimals":"5.0","display_name":"Dummy External Provider","supplier_score":null},"vehicle_type":{"key":21,"name":"Bus"}}}],"ticket_data":{},"ticket_types":null,"pass_types":null,"amenities":[{"key":"wifi","name":"WiFi","description":"Connect to wireless internet in your car.","image_url":"https://static.mozio.com/amenities/wifi.svg","png_image_url":"https://static.mozio.com/amenities/wifi.png","input_type":"boolean","included":false,"selected":false,"internal":false,"price":{"value":"10.00","display":"$10.00","compact":"$10","currency":"USD"},"price_usd":"10.00"},{"key":"sms_notifications","name":"SMS Notification","description":"Receive SMS notification about your reservation status updates","image_url":"https://static.mozio.com/amenities/sms-notification.svg","png_image_url":"https://static.mozio.com/amenities/sms-notification.png","input_type":"boolean","included":false,"selected":false,"internal":true,"price":{"value":"1.50","display":"$1.50","compact":"$1.50","currency":"USD"},"price_usd":"1.50"},{"key":"wheelchair","name":"Wheelchair accessible","description":"This vehicle provides a ramp or lift to accommodate passengers in wheelchairs.","image_url":"https://static.mozio.com/amenities/wheelchair.svg","png_image_url":"https://static.mozio.com/amenities/wheelchair.png","input_type":"boolean","included":false,"selected":false,"internal":false,"price":{"value":"15.00","display":"$15.00","compact":"$15","currency":"USD"},"price_usd":"15.00"},{"key":"english","name":"English speaking driver","description":"The driver will speak English, in addition to the local language.","image_url":"https://static.mozio.com/amenities/english.svg","png_image_url":"https://static.mozio.com/amenities/english.png","input_type":"boolean","included":true,"selected":false,"internal":false,"price":{"value":"0.00","display":"$0.00","compact":"$0.00","currency":"USD"},"price_usd":"0.00"},{"key":"power","name":"In-seat power","description":"Charge devices while you travel.","image_url":"https://static.mozio.com/amenities/power.svg","png_image_url":"https://static.mozio.com/amenities/power.png","input_type":"boolean","included":true,"selected":false,"internal":false,"price":{"value":"0.00","display":"$0.00","compact":"$0.00","currency":"USD"},"price_usd":"0.00"},{"key":"ride_tracking","name":"Ride tracking","description":"Monitor the location of your vehicle in real-time.","image_url":"https://static.mozio.com/amenities/tracking.svg","png_image_url":"https://static.mozio.com/amenities/tracking.png","input_type":"boolean","included":true,"selected":false,"internal":false,"price":{"value":"0.00","display":"$0.00","compact":"$0.00","currency":"USD"},"price_usd":"0.00"},{"key":"restroom","name":"Onboard restroom","description":"Bathrooms are available in the vehicle.","image_url":"https://static.mozio.com/amenities/restrooms.svg","png_image_url":"https://static.mozio.com/amenities/restrooms.png","input_type":"boolean","included":true,"selected":false,"internal":false,"price":{"value":"0.00","display":"$0.00","compact":"$0.00","currency":"USD"},"price_usd":"0.00"}],"hourly_details":{"original_requested":0,"hours_requested":0,"minimum":1,"included_kilometers_per_hour":20,"total_included_kilometers":0},"flt_support":false},"can_cancel":true,"mozio_profit_usd":"10.00","partner_profit_usd":"0.00","gross_revenue_usd":"60.00","mozio_profit":"10.00","partner_profit":"0.00","gross_revenue":"60.00","credit_card":{"last4":"****","brand":""},"campaign":"Your Full Name","branch":"","cancelled":false,"timestamp":"2023-07-15T00:04:11Z","cancelled_timestamp":"","rebooked_id":null,"total_price":{"value":"60.00","display":"$60.00","compact":"$60"},"vat_amount":null,"nonrefundable_amount":{"value":"0.00","display":"$0.00","compact":"$0.00"},"phone_number_national":8776649925,"phone_number_country_code_name":"US","is_delayed_flight_info":false,"offers":{"extra_trip_offer":{"extra_trip_search_link":"https://www.mozio.com/en-us/?utm_source=btp&utm_medium=btp&utm_campaign=Extra+Trip+Upsell&campaign=OneWayUpsell&num_passengers=2&start_address=PHL&pickup_datetime=12%2F01%2F2023+02%3A30+PM&coupon_code=XTRIP_XAUIO","extra_trip_iata_code":"PHL","trip_direction":"from","extra_trip_coupon_percentage":10,"extra_trip_coupon_code":"XTRIP_XAUIO"}},"has_passed":false,"currency":"USD","provider":{"id":1688,"uid":"749fe9b8-a492-4a3f-b7fc-4fa15b046409","name":"Dummy External Provider","is_active":true,"url":null,"report_currency":"USD","email":"info@mozio.com","phone_number":"+3903827802737","logo_url":"https://static.mozio.com/providers/logos/defaults/blackcar_logo.png","rating":5,"options":{"twentyfour_hour_time":false},"description":null,"has_terms":false},"email":"happytraveler9@mozio.com","phone_number":"+1 877-664-9925","first_name":"Happy9","last_name":"Traveler9","airline":"AA","flight_number":"259","airport_terminal":"","pickup_time_buffer":null,"customer_special_instructions":"My dolorbbell is brokennn, pleasee yell","partner_tracking_id":"","consent_for_contact":false,"extra_pax_info":[],"cruise_line":"","ship_name":"","train_company":null,"train_number":null,"return_train_company":"","return_train_number":"","flight_type":"","google_analytics_client_id":"","loyalty":null}]}
Reservation ID: ef43cc6b912441afb64c33f3c42cd137
Confirmation Number: DUM88412283
Booking Successful!
Confirmation Number: DUM88412283
Booking Canceled:
{'refunded': 1, 'cancelled': 1, 'coupon_code': None}

<img width="1157" alt="image" src="https://github.com/saminov19/mozio_task/assets/39556766/c59a6190-6ca7-4c08-9a93-96383204667c">

