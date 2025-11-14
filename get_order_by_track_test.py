import sender_stand_request
import data

def get_track(body):
    response = sender_stand_request.post_new_order(body)
    return response.json()["track"]

def test_positive_assert():
    assert_body = data.order_body.copy()
    sender_stand_request.post_new_order(assert_body)
    assert_track_response = str(get_track(assert_body))
    order_response = sender_stand_request.get_order_by_track(assert_track_response)
    assert order_response.status_code == 200

