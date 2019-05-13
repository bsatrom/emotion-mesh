# emotion-mesh

The Emotion Mesh project is a demonstration of using Edge Machine Learning and IoT with Particle 3rd Generation, mesh-capable devices (Argon, Xenon) and the Google Coral Dev Board, which contains an ML-capable Edge TPU module.

This repository is broken up into sub-projects that each manage one aspect of the demo. The main demo sequence and major components are sequenced below.

## Emotion Mesh Flow

![](/assets/EmotionMesh.png)

1. **[Idle State]** Between runs of the Emotion Mesh Demo, the network is in the following state:
  a. Coral-connected webcam is off
  b. Coral-connected Monitor hides the webcam view and displays full-screen statistics about previous runs
  c. Neopixels play an attract animation
  d. Green and Red buttons are off
  c. Ultrasonic distance sensor is active and looking for a person to step into the demo area, which triggers the Capture State

2. **[Capture State]**
  a. Webcam is activated
  b. Monitor shows live webcam view with Face Tracking and instructions for the user to convey an emotion (happy, sad, etc.) and hit the green button to capture a photo for processing.
  c. Green and Red buttons light up.
    - Green captures a photo and transitions to Processing State.
    - Red cancels the demo and returns to Idle State.
  d. Neopixels transition into a pulse animation.

3. **[Processing State]**
  a. Webcam is turned off.
  b. Monitor shows processing still photo and a processing message.
  c. Green and Red buttons are turned off.
  d. Neopixels transition to a loading/processing animations.
  e. Coral Dev Board submits photo for local and cloud processing
    - **[Local Processing]** Use the Coral Edge TPU module to process the captured still, and use the result to mark up a copy of the image.
    - **[Cloud Processing]** Use the Azure ML Face API to send the captured still, and use the result to mark up a copy of the image. 

4.**[Results State]**
  a. Monitor shows the processed still photo from the local run and asks the user to hit green button if the emotion was interpreted correctly, and red if not. 
  b. Green and Red Buttons are activated and waiting for a response.
  c. Neopixels return to a pulsing/waiting state.
  d. Once the user taps a button, demo moves into Response state.

5. **[Response State]**
  a. Monitor shows the yes/no response and updates running statistics. Monitor also shows the cloud detector result if it differs from the local.
  b. Ultrasonic is re-activated.
  c. Neopixels turn green if the detector was correct and red, if not.

6. Once the individual leaves the demo space and the Ultrasonic distance sensor detects its baseline reading, the demo returns to idle state.

## Emotion Mesh Hardware

- Google Coral Dev Board
  - Logitech 1080p Webcam
  - 27-inch monitor
- Particle Argon
  - Mesh Network Gateway Device
  - Connected to Coral Dev Board via UART
  - 100mm Arcade Buttons (Red and Green) connected to Argon
- 1x Particle Xenon & Ultrasonic Distance Sensor
- 4x Particle Xenon & Adafruit Neopixel Strips

## Emotion Mesh Cloud Dashboard

In addition to local capabilities, this project also demonstrates using the Particle Device Cloud and Azure IoT Central for cloud processing and insight. 

[Details TBD]

## Emotion Mesh Live Statistics

The local dashboard view of the Emotion Mesh project shows the following metrics:

- No. of images processed
- % of local emotions detected correctly/incorrectly
- % of cloud emotions (Azure Face API) detected correctly/incorrectly
- % of each emotion detected
- Time to local result vs. time to cloud result (incl. latency)
- Variance between local face detection results and cloud results