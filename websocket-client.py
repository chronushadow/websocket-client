#!/usr/bin/env python

import websocket
import rospy
from std_msgs.msg import String
import sys
import threading
import ssl
from datetime import datetime

def callback(data, *args):
    rospy.loginfo("Subscribe: %s", data.data)

    msg = datetime.now().isoformat()
    rospy.loginfo("Ping: %s", msg)

    ws = args[0]
    ws.send(msg)

def subscribe(ws):
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber("hello", String, callback, (ws))
    rospy.spin()

def on_open(ws):
    print("Connected WebSocket server")

def on_message(ws, msg):
    recieved_time = datetime.now()

    print("Pong: {0}".format(msg))
    print("Now: {0}".format(recieved_time))
    server_send_time = datetime.strptime(msg, '%Y-%m-%dT%H:%M:%S.%f')
    print("Time from server to client: {0}".format(recieved_time - server_send_time))

def on_close(ws):
    print("Disconnected WebSocket server")

def on_error(ws, error):
    print(error)

sslopt = {"cert_reqs": ssl.CERT_NONE}

if __name__ == '__main__':

    argv = sys.argv
    url = argv[1]

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)

    wst = threading.Thread(target=ws.run_forever, args=(None, sslopt))
    wst.daemon = True
    wst.start()

    subscribe(ws)
