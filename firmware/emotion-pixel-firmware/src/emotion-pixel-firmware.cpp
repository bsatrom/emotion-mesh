#include "Particle.h"
#include "neopixel.h"
#include "math.h"

/*
 * Project emotion-pixel-firmware
 * Description:
 * Author:
 * Date:
 */

#define PIXEL_PIN D2
#define PIXEL_COUNT 30
#define PIXEL_TYPE WS2812B
#define BRIGHTNESS 50

int mode = 0; // 0 = IDLE, 1 = CAPTURE, 2 = WAITING, 3 = CORRECT, 4 = INCORRECT

Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, PIXEL_TYPE);

void rainbow(uint8_t wait);
uint32_t Wheel(byte WheelPos);
int adjustBrightness(String args);
void handleIdle(const char *event, const char *payload);
void handleCapture(const char *event, const char *payload);
void handleWaiting(const char *event, const char *payload);
void handleCorrect(const char *event, const char *payload);
void handleIncorrect(const char *event, const char *payload);

void NewKITT(byte red, byte green, byte blue, int EyeSize, int SpeedDelay, int ReturnDelay);
void RunningLights(byte red, byte green, byte blue, int WaveDelay);
void theaterChase(byte red, byte green, byte blue, int SpeedDelay);

void setup()
{
  strip.setBrightness(BRIGHTNESS);
  strip.begin();
  strip.show();

  Particle.function("adjBright", adjustBrightness);

  Mesh.subscribe("state/idle", handleIdle);
  Mesh.subscribe("state/capture", handleCapture);
  Mesh.subscribe("state/waiting", handleWaiting);
  Mesh.subscribe("state/correct", handleCorrect);
  Mesh.subscribe("state/incorrect", handleIncorrect);
}

void loop()
{
  if (mode == 0)
  {
    // Idle Animation
    NewKITT(0xff, 0, 0, 8, 10, 50);
  }
  else if (mode == 1)
  {
    rainbow(20);
  }
  else if (mode == 2)
  {
    // Waiting Animation
    RunningLights(0xff, 0xff, 0x00, 50);
  }
  else if (mode == 3)
  {
    // Inference was correct
    theaterChase(0, 0xff, 0, 50); // Green
  }
  else if (mode == 4)
  {
    // Inference was incorrect
    theaterChase(0xff, 0, 0, 50); // Red
  }
}

int adjustBrightness(String args)
{
  int brightness = args.toInt();
  uint16_t i;

  if (brightness > 0)
  {
    strip.setBrightness(brightness);
    strip.show();

    return 1;
  }

  return 0;
}

void handleIdle(const char *event, const char *payload)
{
  mode = 0;
}

void handleCapture(const char *event, const char *payload)
{
  mode = 1;
}

void handleWaiting(const char *event, const char *payload)
{
  mode = 2;
}

void handleCorrect(const char *event, const char *payload)
{
  mode = 3;
}

void handleIncorrect(const char *event, const char *payload)
{
  mode = 4;
}

void rainbow(uint8_t wait)
{
  uint16_t i, j;

  for (j = 0; j < 256; j++)
  {
    for (i = 0; i < strip.numPixels(); i++)
    {
      strip.setPixelColor(i, Wheel((i + j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos)
{
  if (WheelPos < 85)
  {
    return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
  }
  else if (WheelPos < 170)
  {
    WheelPos -= 85;
    return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  }
  else
  {
    WheelPos -= 170;
    return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
}

void showStrip()
{
  // NeoPixel
  strip.show();
}

void setPixel(int Pixel, byte red, byte green, byte blue)
{
  // NeoPixel
  strip.setPixelColor(Pixel, strip.Color(red, green, blue));
}

void setAll(byte red, byte green, byte blue)
{
  for (int i = 0; i < PIXEL_COUNT; i++)
  {
    setPixel(i, red, green, blue);
  }
  showStrip();
}

void theaterChase(byte red, byte green, byte blue, int SpeedDelay)
{
  for (int j = 0; j < 10; j++)
  { //do 10 cycles of chasing
    for (int q = 0; q < 3; q++)
    {
      for (int i = 0; i < PIXEL_COUNT; i = i + 3)
      {
        setPixel(i + q, red, green, blue); //turn every third pixel on
      }
      showStrip();

      delay(SpeedDelay);

      for (int i = 0; i < PIXEL_COUNT; i = i + 3)
      {
        setPixel(i + q, 0, 0, 0); //turn every third pixel off
      }
    }
  }
}

void RunningLights(byte red, byte green, byte blue, int WaveDelay)
{
  int Position = 0;

  for (int i = 0; i < PIXEL_COUNT * 2; i++)
  {
    Position++; // = 0; //Position + Rate;
    for (int i = 0; i < PIXEL_COUNT; i++)
    {
      // sine wave, 3 offset waves make a rainbow!
      //float level = sin(i+Position) * 127 + 128;
      //setPixel(i,level,0,0);
      //float level = sin(i+Position) * 127 + 128;
      setPixel(i, ((sin(i + Position) * 127 + 128) / 255) * red,
               ((sin(i + Position) * 127 + 128) / 255) * green,
               ((sin(i + Position) * 127 + 128) / 255) * blue);
    }

    showStrip();
    delay(WaveDelay);
  }
}

void CenterToOutside(byte red, byte green, byte blue, int EyeSize, int SpeedDelay, int ReturnDelay)
{
  for (int i = ((PIXEL_COUNT - EyeSize) / 2); i >= 0; i--)
  {
    setAll(0, 0, 0);

    setPixel(i, red / 10, green / 10, blue / 10);
    for (int j = 1; j <= EyeSize; j++)
    {
      setPixel(i + j, red, green, blue);
    }
    setPixel(i + EyeSize + 1, red / 10, green / 10, blue / 10);

    setPixel(PIXEL_COUNT - i, red / 10, green / 10, blue / 10);
    for (int j = 1; j <= EyeSize; j++)
    {
      setPixel(PIXEL_COUNT - i - j, red, green, blue);
    }
    setPixel(PIXEL_COUNT - i - EyeSize - 1, red / 10, green / 10, blue / 10);

    showStrip();
    delay(SpeedDelay);
  }
  delay(ReturnDelay);
}

void OutsideToCenter(byte red, byte green, byte blue, int EyeSize, int SpeedDelay, int ReturnDelay)
{
  for (int i = 0; i <= ((PIXEL_COUNT - EyeSize) / 2); i++)
  {
    setAll(0, 0, 0);

    setPixel(i, red / 10, green / 10, blue / 10);
    for (int j = 1; j <= EyeSize; j++)
    {
      setPixel(i + j, red, green, blue);
    }
    setPixel(i + EyeSize + 1, red / 10, green / 10, blue / 10);

    setPixel(PIXEL_COUNT - i, red / 10, green / 10, blue / 10);
    for (int j = 1; j <= EyeSize; j++)
    {
      setPixel(PIXEL_COUNT - i - j, red, green, blue);
    }
    setPixel(PIXEL_COUNT - i - EyeSize - 1, red / 10, green / 10, blue / 10);

    showStrip();
    delay(SpeedDelay);
  }
  delay(ReturnDelay);
}

void LeftToRight(byte red, byte green, byte blue, int EyeSize, int SpeedDelay, int ReturnDelay)
{
  for (int i = 0; i < PIXEL_COUNT - EyeSize - 2; i++)
  {
    setAll(0, 0, 0);
    setPixel(i, red / 10, green / 10, blue / 10);
    for (int j = 1; j <= EyeSize; j++)
    {
      setPixel(i + j, red, green, blue);
    }
    setPixel(i + EyeSize + 1, red / 10, green / 10, blue / 10);
    showStrip();
    delay(SpeedDelay);
  }
  delay(ReturnDelay);
}

void RightToLeft(byte red, byte green, byte blue, int EyeSize, int SpeedDelay, int ReturnDelay)
{
  for (int i = PIXEL_COUNT - EyeSize - 2; i > 0; i--)
  {
    setAll(0, 0, 0);
    setPixel(i, red / 10, green / 10, blue / 10);
    for (int j = 1; j <= EyeSize; j++)
    {
      setPixel(i + j, red, green, blue);
    }
    setPixel(i + EyeSize + 1, red / 10, green / 10, blue / 10);
    showStrip();
    delay(SpeedDelay);
  }
  delay(ReturnDelay);
}

void NewKITT(byte red, byte green, byte blue, int EyeSize, int SpeedDelay, int ReturnDelay)
{
  RightToLeft(red, green, blue, EyeSize, SpeedDelay, ReturnDelay);
  LeftToRight(red, green, blue, EyeSize, SpeedDelay, ReturnDelay);
  OutsideToCenter(red, green, blue, EyeSize, SpeedDelay, ReturnDelay);
  CenterToOutside(red, green, blue, EyeSize, SpeedDelay, ReturnDelay);
  LeftToRight(red, green, blue, EyeSize, SpeedDelay, ReturnDelay);
  RightToLeft(red, green, blue, EyeSize, SpeedDelay, ReturnDelay);
  OutsideToCenter(red, green, blue, EyeSize, SpeedDelay, ReturnDelay);
  CenterToOutside(red, green, blue, EyeSize, SpeedDelay, ReturnDelay);
}