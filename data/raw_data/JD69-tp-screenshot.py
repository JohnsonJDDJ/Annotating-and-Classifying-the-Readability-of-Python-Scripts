import rel
import websocket
import json
import time
import os

import pyautogui as pagui
import cv2 as cv
import numpy as np

import ssl


screen_wid = 1920
screen_hei = 1200
img_wid = screen_wid
img_hei = int(screen_wid / 3)

y_plus = -5

y, x, h, w = int((screen_hei - img_hei) / 2) + y_plus, 0, img_hei, img_wid
dim = (y, x, y + h, x + w)

# ws_url = "wss://wss.2enter.art/dvtp/"
ws_url = "wss://wss.2enter.art/dvtp/"
img_dir = "./dvtp-screenshots"
img_format = "jpg"


def parse_msg(message):
    message = json.loads(str(message))
    return message


def take_shot(_id):
    # image = pagui.screenshot()
    # image = cv.cvtColor(np.array(pagui.screenshot()), cv.COLOR_RGB2BGR)
    screenshot_image = pagui.screenshot()
    screenshot_image = cv.cvtColor(np.array(screenshot_image), cv.COLOR_BGR2RGB)

    # pagui.screenshot(f"{img_dir}/{_id}.{img_format}")
    # time.sleep(2)
    # screenshot_image = cv.imread(f"{img_dir}/{_id}.{img_format}")

    cropped = np.array(screenshot_image)[y : y + h, x : x + w]

    # resized = cv.resize(cropped, (1500, 844), interpolation=cv.INTER_AREA)

    cv.imwrite(f"{img_dir}/{_id}.{img_format}", cropped)
    print(f"ScreenShot Taken~ key: {_id}")


def on_message(ws, message):
    message = parse_msg(message)
    if message["ws_type"] == "button":
        print(message["_id"])
        take_shot(message["_id"])
    else:
        print(f"It's a {message['ws_type']} type of msg. Not a button msg")
        # print(message)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    print("Opened connection")


def ws_connection(ws_url):
    ws = websocket.WebSocketApp(
        ws_url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    return ws


ws_client = ws_connection(ws_url)

ws_client.run_forever(
    dispatcher=rel,
    reconnect=5,
    sslopt={"cert_reqs": ssl.CERT_NONE},
)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly

rel.signal(2, rel.abort)  # Keyboard Interrupt
rel.dispatch()