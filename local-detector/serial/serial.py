# Set-up a Serial Connection between the Argon and Coral Dev Board
from periphery import Serial
from time import sleep
import signal
import sys
from websocket import create_connection
import socket

sock_ip = "192.168.10.216:4664"

# import protobuf
sys.path.insert(0, '/home/mendel/emotion-mesh/local-detector/streaming')
import proto.messages_pb2 as messages_pb2

# UART 1 on the Coral
serial = Serial("/dev/ttymxc0", 115200)

def signal_handler(signal, frame):
    print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
    serial.close()
    exit(0)

print('Waiting for a message from the Argon...')

signal.signal(signal.SIGINT, signal_handler)

def capture_image():
  print('Opening websocket connection to server...')
  message = messages_pb2.ServerBound()
  message.frame_capture.overlay = True
  
  ws = create_connection("ws://" + sock_ip + "/stream")
  print('Socket open, sending capture command...')
  
  ws.send_binary(message.SerializeToString())
  print('Message sent...')
  sleep(1)
  print('Sending response to controller...')
  serial.write(b'1\n')
  serial.flush()
  print('Closing socket...')
  ws.close()


# wait for something from the Argon to trigger the demo
while True:
  if (serial.poll(timeout=1)):
    buf = serial.read(128, 0.5)
    serial_message = str(buf, 'utf-8').strip()
    print("read %d bytes: %s" % (len(buf), serial_message))
    
    if (serial_message == 'capture'):
      capture_image()
    elif (serial_message == 'reset'):
      print('Resetting...')
    elif (serial_message == 'yes'):
      print('Emotion inference was right!')
    elif (serial_message == 'no'):
      print('Emotion inference was wrong!')
    
