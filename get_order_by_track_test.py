import configuration
import sender_stand_request
import data
import requests


def get_track():
    response = sender_stand_request.post_new_order(data.order_body)
    return response.json()["track"]

track_response = str(get_track())

def get_order_by_track():
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_PATH + track_response)

def test_possitive_assert():
    order_response = get_order_by_track()
    assert order_response.status_code == 200