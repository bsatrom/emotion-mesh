# Set-up a Serial Connection between the Argon and Coral Dev Board
from periphery import Serial
from time import sleep
import signal
import sys
import websocket
import socket, threading

# UART 1 on the Coral
serial = Serial("/dev/ttymxc2", 115200)
sock_ip = "192.168.1.235:4665" # Update with IP

# import protobuf
sys.path.insert(0, '/home/mendel/emotion-mesh/local-detector/streaming')
import proto.messages_pb2 as messages_pb2

def start_serial(ws):
  print('Waiting for a message from the Argon...')
  
  # wait for something from the Argon to trigger the demo
  while True:
    if (serial.poll(timeout=1)):
      buf = serial.read(128, 0.5)
      serial_message = str(buf, 'utf-8').strip()
      print("read %d bytes: %s" % (len(buf), serial_message))
      
      if (serial_message == 'capture'):
        capture_image(serial, ws)
      elif (serial_message == 'reset'):
        send_reset(ws)
      elif (serial_message == 'yes'):
        print('Emotion inference was right!')
        send_response(ws, True)
      elif (serial_message == 'no'):
        print('Emotion inference was wrong!')
        send_response(ws, False)

def capture_image(serial, ws):
  message = messages_pb2.ServerBound()
  message.frame_capture.overlay = True
  
  print('Sending capture command...')
  
  ws.send(message.SerializeToString(), 0x2)
  print('Message sent...')

def send_reset(ws):
  message = messages_pb2.ServerBound(reset=messages_pb2.Reset())  
  print('Resetting...')
  ws.send(message.SerializeToString(), 0x2)
      
def send_response(ws, isCorrect):
  message = messages_pb2.ServerBound()
  message.response.correct = isCorrect
  print('Sending inference response...')
  ws.send(message.SerializeToString(), 0x2)

def on_open(ws):
  print('#### Websocket opened ####')

def on_message(ws, message):
    msg = messages_pb2.ClientBound()
    msg.ParseFromString(message)
    which = msg.WhichOneof('message')
    if which == 'detectionResult':
      emotionResult = eval(msg.detectionResult.emotionResult)
      if not emotionResult:
        print('No emotion result detected. Issuing reset command to controller via UART.')
        serial.write(b'2\n')
      else:
        print('Sending response to controller...')
        serial.write(b'1\n')
      serial.flush()

def on_error(ws, error):
    print('Websocket error: ' + str(error))

def on_close(ws):
    print('#### Websocket Closed ####')

# Create threads for UART and WebSocket
if __name__ == '__main__':
  print('Opening websocket connection to server...')
  websocket.enableTrace(True)
  ws = websocket.WebSocketApp("ws://" + sock_ip + "/stream",
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close)
  
  serial_thread = threading.Thread(target=start_serial, args=(ws,))
  serial_thread.start()
  
  ws.on_open = on_open
  ws.run_forever()