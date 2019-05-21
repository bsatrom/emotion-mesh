#include "application.h"
/*
 * Project emotion-controller
 * Description:
 * Author:
 * Date:
 */

int sendSerial(String args)
{
  Serial1.println("capture");
  return 1;
}

void setup()
{
  Serial1.begin(9600);

  Particle.function("sendSerial", sendSerial);
}

void loop()
{
}