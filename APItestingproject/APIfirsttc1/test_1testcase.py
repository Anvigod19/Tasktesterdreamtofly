import os
import dotenv
from dotenv import load_dotenv
import allure


import pytest
import requests

@pytest.mark.smoke
@allure.feature("TC1 verify get request")
def test_get_req():
    response = requests.get("https://restful-booker.herokuapp.com/booking")
    print(response.status_code)
    assert response.status_code == 200

@allure.feature("TC2 verify post request")
def test_post_create_booking():
    load_dotenv()
    payload_create_booking = {
        "firstname": "Pramod",
        "lastname": "Dutta",
        "totalprice": 10000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2022-12-28",
            "checkout": "2023-01-02"
        },
        "additionalneeds": "Breakfast"
    }

    headers = {
        "Content-Type": "application/json",
    }
    # Additonal Information that we need to send the to Server to let server know that we are
    # sending a json payload in the request

    response = requests.post("https://restful-booker.herokuapp.com/booking", headers=headers,
                             json=payload_create_booking)
    print(response.json())
    booking_id = response.json()["bookingid"]
    print(booking_id)
    print(response.headers)
    assert response.status_code == 200
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",os.getenv("username1"))

    # More Assert - More No of Testcases - More No Assertion
    # Passing the data between the Testcases

