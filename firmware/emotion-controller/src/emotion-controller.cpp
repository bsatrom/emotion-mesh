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
#define GREEN_BUTTTON D3
#define RED_LED D4
#define RED_BUTTON D4

#define IDLE_TOGGLE_DELAY 5000

void configureIdle();
void configureCapture();
void configureResponse();
void configureReset();
void resetLEDs();

// STATES
State Idle = State(configureIdle);
State Capture = State(configureCapture);
State Response = State(configureResponse);
State Reset = State(configureReset);

FSM controllerFSM = FSM(Idle);
bool toggleState = true;

unsigned long lastToggleMillis = 0;

int sendSerial(String args)
{
  Serial1.println(args);

  return 1;
}

void setup()
{
  Serial1.begin(9600);

  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(GREEN_BUTTTON, INPUT_PULLUP);
  pinMode(RED_BUTTON, INPUT_PULLDOWN);

  resetLEDs();

  Particle.publish("button-state", (String)digitalRead(GREEN_BUTTTON));

  Particle.function("sendSerial", sendSerial);
}

void loop()
{
  unsigned long currentMillis = millis();

  if (controllerFSM.isInState(Idle) && currentMillis - lastToggleMillis > IDLE_TOGGLE_DELAY)
  {
    lastToggleMillis = millis();
    digitalWrite(GREEN_LED, toggleState);
    digitalWrite(RED_LED, !toggleState);

    toggleState = !toggleState;
  }

  if (controllerFSM.isInState(Capture))
  {
  }
}

void resetLEDs()
{
  digitalWrite(GREEN_LED, LOW);
  digitalWrite(RED_LED, LOW);
}

void configureIdle()
{
  resetLEDs();
}

void configureCapture()
{
  resetLEDs();

  digitalWrite(GREEN_LED, HIGH);
}

void configureResponse()
{
  digitalWrite(GREEN_LED, HIGH);
  digitalWrite(RED_BUTTON, HIGH);
}