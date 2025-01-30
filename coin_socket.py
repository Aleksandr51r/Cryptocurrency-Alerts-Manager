import websocket
import json


def on_message(ws, message):
    # Выводим сообщение с сервера
    data = json.loads(message)
    if data.get("type") == "trade":
        # print(data)
        if data['symbol_id'] == 'BITSTAMP_SPOT_BTC_USD':
            print(
                f"TRADE | BTC/USD | Price: {data['price']} | Size: {data['size']} | Time: {data['time_exchange']}")
        elif data['symbol_id'] == 'BITSTAMP_SPOT_ETH_USD':
            print(
                f"TRADE | ETH/USD | Price: {data['price']} | Size: {data['size']} | Time: {data['time_exchange']}")


def on_error(ws, error):
    print(f"Error: {error}")


def on_close(ws, close_status_code, close_msg):
    print("Connection closed")


def on_open(ws):
    # Подписка на поток сделок (trades) для BTC/USD
    subscribe_message = {
  "type": "subscribe",
  "heartbeat": True,
  "subscribe_filter_asset_id": ["ETH/CNY"]
}
    # {
    #     "type": "hello",
    #     # "apikey": "5cba0eef-fd97-470f-99be-bb5757f150f0",  # Вставь свой API-ключ
    #     "heartbeat": False,        # Для проверки активности соединения

    #     "subscribe_filter_asset_id": ["BTC/USD"]
    # }

    # .,"BITSTAMP_SPOT_ETH_USD"

    ws.send(json.dumps(subscribe_message))
    print("Subscribed to BTC/USD trades")


# Адрес WebSocket CoinAPI
websocket_url = "wss://ws.coinapi.io/v1/"

# Инициализация WebSocket
ws = websocket.WebSocketApp(websocket_url,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.on_open = on_open
ws.run_forever()
