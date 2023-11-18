import configuration
import requests
import data


# Функция для создания заказа
def post_new_order():
    return requests.post(
        configuration.URL_SERVICE + configuration.POST_ORDER,
        json=data.order_body,
        headers=data.headers,
    )


# Функция для получения заказа по трек-номеру
def get_order_by_track(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_TRACK,
        params={"t": track},
        headers=data.headers,
    )
