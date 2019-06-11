#include "application.h"
#include "FiniteStateMachine.h"
#include "Debounce.h"

/*
 * Project emotion-controller
 * Description: Firmware to control a arcade-button box with a Serial connection 
 *  to a Google Coral board
 * Author: Brandon Satrom <brandon@particle.io>
 * Date:
 */

#define GREEN_LED D2
#define GREEN_BUTTON D3
#define RED_LED D4
#define RED_BUTTON D5

#define IDLE_TOGGLE_DELAY 3000
#define DEBOUNCE_DELAY 100

// State Functions
void configureIdle();
void updateIdle();
void exitIdle();
void configureCapture();
void updateCapture();
void exitCapture();
void configureWaiting();
void updateWaiting();
void exitWaiting();
void configureResponse();
void updateResponse();
void exitResponse();

// Event Functions
int triggerCapture(String args);
int triggerIdle(String args);
int triggerWaiting(String args);
int triggerCorrect(String args);
int triggerIncorrect(String args);

// Utility functions
void resetLEDs();

Debounce greenDebouncer = Debounce();
Debounce redDebouncer = Debounce();

// STATES
State Idle = State(configureIdle, updateIdle, exitIdle);
State Capture = State(configureCapture, updateCapture, exitCapture);
State Waiting = State(configureWaiting, updateWaiting, exitWaiting);
State Response = State(configureResponse, updateResponse, exitResponse);

// FSM states constants
#define STATE_IDLE "Idle"
#define STATE_CAPTURE "Capture"
#define STATE_WAITING "Waiting"
#define STATE_RESPONSE "Response"
String state = STATE_IDLE;
String lastState = "";

FSM controllerFSM = FSM(Idle);
bool toggleState = true;
bool captureSent = false;
bool responseCaptured = false;

unsigned long lastToggleMillis = 0;

const size_t READ_BUF_SIZE = 64;
char readBuf[READ_BUF_SIZE];
size_t readBufOffset = 0;

int sendSerial(String args)
{
  Serial1.println(args);

  return 1;
}

void setState(String newState, bool setLastState)
{
  state = newState;
  if (setLastState)
  {
    lastState = newState;
  }

  Particle.publish("state-update", "FSM entering " + newState + " state", PRIVATE);
}

void setup()
{
  Serial1.begin(115200);

  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);

  greenDebouncer.attach(GREEN_BUTTON, INPUT_PULLUP);
  greenDebouncer.interval(DEBOUNCE_DELAY);

  redDebouncer.attach(RED_BUTTON, INPUT_PULLUP);
  redDebouncer.interval(DEBOUNCE_DELAY);

  resetLEDs();

  Particle.function("sendSerial", sendSerial);
  Particle.function("tgCap", triggerCapture);
  Particle.function("tgIdle", triggerIdle);
  Particle.function("tgWait", triggerWaiting);
  Particle.function("tgCorrect", triggerCorrect);
  Particle.function("tgIncorrect", triggerIncorrect);
  Particle.variable("state", state);
}

void loop()
{
  controllerFSM.update();
}

void resetLEDs()
{
  digitalWrite(GREEN_LED, LOW);
  digitalWrite(RED_LED, LOW);
}

void configureIdle()
{
  setState(STATE_IDLE, true);
  resetLEDs();

  Mesh.publish("state/idle", NULL);
}

void updateIdle()
{
  unsigned long currentMillis = millis();

  if (currentMillis - lastToggleMillis > IDLE_TOGGLE_DELAY)
  {
    lastToggleMillis = millis();
    digitalWrite(GREEN_LED, toggleState);
    digitalWrite(RED_LED, !toggleState);

    toggleState = !toggleState;
  }

  if (greenDebouncer.update() && greenDebouncer.read() == LOW)
  {
    sendSerial("reset");

    controllerFSM.transitionTo(Capture);
  }
}

void exitIdle()
{
  resetLEDs();
}

void configureCapture()
{
  setState(STATE_CAPTURE, true);

  digitalWrite(GREEN_LED, HIGH);

  Mesh.publish("state/capture", NULL);
}

void updateCapture()
{
  if (greenDebouncer.update() && greenDebouncer.read() == LOW && !captureSent)
  {
    captureSent = true;
    sendSerial("capture");

    controllerFSM.transitionTo(Waiting);
  }
  else if (redDebouncer.update() && redDebouncer.read() == LOW && !captureSent)
  {
    controllerFSM.transitionTo(Idle);
  }
}

void exitCapture()
{
  captureSent = false;
}

void configureWaiting()
{
  setState(STATE_WAITING, true);

  digitalWrite(GREEN_LED, HIGH);
  digitalWrite(RED_BUTTON, HIGH);

  Mesh.publish("state/waiting", NULL);
}

void updateWaiting()
{
  // Read from Serial for a response
  while (Serial1.available())
  {
    if (readBufOffset < READ_BUF_SIZE)
    {
      char c = Serial1.read();
      if (c != '\n')
      {
        // Add character to buffer
        readBuf[readBufOffset++] = c;
      }
      else
      {
        // End of line character found, process line
        if (atoi(readBuf) == 1) // Face Found
        {
          controllerFSM.transitionTo(Response);
        }
        else if (atoi(readBuf) == 2) // No Face Found
        {
          controllerFSM.transitionTo(Capture);
        }

        readBuf[readBufOffset] = 0;
        readBufOffset = 0;

        break;
      }
    }
    else
    {
      // Empty buffer
      readBufOffset = 0;
    }
  }
}

void exitWaiting()
{
  resetLEDs();
}

void configureResponse()
{
  setState(STATE_RESPONSE, true);

  digitalWrite(GREEN_LED, HIGH);
  digitalWrite(RED_LED, HIGH);

  Mesh.publish("state/response", NULL);
}

void updateResponse()
{
  if (greenDebouncer.update() && greenDebouncer.read() == LOW && !responseCaptured)
  {
    responseCaptured = true;
    sendSerial("yes");

    Mesh.publish("state/correct", NULL);
  }
  else if (redDebouncer.update() && redDebouncer.read() == LOW && !responseCaptured)
  {
    responseCaptured = true;
    sendSerial("no");

    Mesh.publish("state/incorrect", NULL);
  }

  if (responseCaptured)
  {
    delay(10000); // Pause to allow the result to show on the neopixel strips
    controllerFSM.transitionTo(Idle);
  }
}

void exitResponse()
{
  responseCaptured = false;
  resetLEDs();
}

int triggerCapture(String args)
{
  controllerFSM.transitionTo(Capture);

  return 1;
}

int triggerIdle(String args)
{
  controllerFSM.transitionTo(Idle);

  return 1;
}

int triggerWaiting(String args)
{
  controllerFSM.transitionTo(Waiting);

  return 1;
}

int triggerCorrect(String args)
{
  Mesh.publish("state/correct");

  return 1;
}

int triggerIncorrect(String args)
{
  Mesh.publish("state/incorrect");

  return 1;
}
