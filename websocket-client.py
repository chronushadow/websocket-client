import sys
try:
    import thread
except ImportError:
    import _thread as thread
import time
import websocket

def on_open(ws):
  def run(*args):
    print("WebSocket connection opened")

    while(True):
      line = sys.stdin.readline()

      if line != "":
        print("Send message: {0}".format(line))
        ws.send(line)

  thread.start_new_thread(run, ())

def on_message(ws, msg):
  print("Recieved message: {0}".format(msg))

def on_close(ws):
  print("Disconnected WebSocket server")

def on_error(ws, error):
  print(error)

if __name__ == '__main__':

  args = sys.argv

  if len(args) == 2:
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(args[1], on_message=on_message, on_error=on_error, on_close=on_close)

    try:
      ws.on_open = on_open
      ws.run_forever()
    except InterruptedError:
      ws.close()
  else:
    print("Please specify the URL as the first argument")


