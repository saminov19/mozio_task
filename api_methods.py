import requests
import json
import time

API_KEY = "6bd1e15ab9e94bb190074b4209e6b6f9"
BASE_URL = "https://api-testing.mozio.com/v2"



def search(start_address, end_address, mode, pickup_datetime, num_passengers, currency, campaign):
    url = f"{BASE_URL}/search/"
    #url = "https://api-testing.mozio.com/v2/search/"

    payload = json.dumps({
        "start_address": start_address,
        "end_address": end_address,
        "mode": mode,
        "pickup_datetime": pickup_datetime,
        "num_passengers": num_passengers,
        "currency": currency,
        "campaign": campaign
    })
    headers = {
      'API-KEY': API_KEY,
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()




def poll_search(search_id):
    url = f"{BASE_URL}/search/{search_id}/poll/"
    headers = {
        'API-KEY': API_KEY
    }

    while True:
        response = requests.request("GET", url, headers=headers)
        print(response.text)
        search_status = response.json()
        if not search_status.get("more_coming", False):
            break
        time.sleep(10)
    
    return search_status



def book(search_id, result_id,email,country_code_name,phone_number,first_name,last_name,airline,flight_number,customer_special_instructions):
    url = f"{BASE_URL}/reservations/"
    payload = json.dumps({
      "search_id": search_id,
      "result_id": result_id,
      "email": email,
      "country_code_name": country_code_name,
      "phone_number": phone_number,
      "first_name": first_name,
      "last_name": last_name,
      "airline": airline,
      "flight_number": flight_number,
      "customer_special_instructions": customer_special_instructions
    })
    headers = {
      'API-KEY': '6bd1e15ab9e94bb190074b4209e6b6f9',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    return response.json()

# results > steps > details > provider_name == "Dummy External Provider" , results > steps > details > price > price > value == min

def poll_booking(search_id):
    url = f"{BASE_URL}/reservations/{search_id}/poll/"
    payload={}
    headers = {
      'API-KEY': API_KEY
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    return response.json()


def cancel_booking(booking_id):
    url = f"{BASE_URL}/reservations/{booking_id}"
    payload={}
    headers = {
      'API-KEY': API_KEY
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    return response.json()
