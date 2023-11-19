from sender_stand_request import post_new_order, get_order_by_track

# Парфенова Ольга, 10-я когорта — Финальный проект. Инженер по тестированию плюс
def test_get_order_by_track():
    response_create_order = post_new_order()
    assert response_create_order.status_code == 201

    track = response_create_order.json()['track']

    response_get_order_by_track = get_order_by_track(track)
    assert response_get_order_by_track.status_code == 200
