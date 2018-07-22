#!/usr/bin/env python

import rospy
import websocket
import threading
from std_msgs.msg import String
import ssl

def callback(data, *args):
    rospy.loginfo(rospy.get_caller_id() + " Subscribe: %s", data.data)

    ws = args[0]
    ws.send(data.data)

def subscribe(ws):
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber("hello", String, callback, (ws))
    rospy.spin()

def on_open(ws):
    print("WebSocket connection opened")

def on_message(ws, msg):
    print("Recieved message: {0}".format(msg))

def on_close(ws):
    print("Disconnected WebSocket server")

def on_error(ws, error):
    print(error)

url = "wss://trial.chronushadow.xyz"
sslopt = {"cert_reqs": ssl.CERT_NONE}

if __name__ == '__main__':

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)

    wst = threading.Thread(target=ws.run_forever, args=(None, sslopt))
    wst.daemon = True
    wst.start()

    subscribe(ws)
