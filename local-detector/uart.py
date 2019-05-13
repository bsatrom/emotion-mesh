# Set-up a UART Connection between the Argon and Coral Dev Board
from periphery import GPIO

# this might need to be Serial instead
coralTX = GPIO(8, "out")
coralRX = GPIO(10, "in")

print(coralTX)
print(coralRX)

# wait for something from the Argon to trigger the demo
# while (true):
  # read from the RX pin
  # coralRX.read()