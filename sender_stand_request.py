import configuration
import requests
import data
import get_order_by_track_test
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDER_PATH, json=body, headers=data.headers)

def get_order_by_track(track_response):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_PATH + track_response)

