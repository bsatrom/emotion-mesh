#include "Particle.h"
#include "Adafruit_GFX.h"
#include "Adafruit_HX8357.h"

#define TFT_DC D5
#define TFT_CS D4
#define STMPE_CS D3
#define SD_CS D2
#define TFT_RST -1

String lastState = "";

Adafruit_HX8357 tft = Adafruit_HX8357(TFT_CS, TFT_DC, TFT_RST);

SerialLogHandler logHandler(LOG_LEVEL_TRACE);

const size_t SCAN_RESULT_MAX = 30;
BleScanResult scanResults[SCAN_RESULT_MAX];

void setup()
{
  (void)logHandler;

  tft.begin();
  tft.fillScreen(HX8357_BLACK);
  tft.setTextSize(3);
  tft.setCursor(45, 20);
  tft.setTextColor(HX8357_WHITE);
  tft.println("#EmotionMesh");
}

void loop()
{
  BLE.setScanTimeout(50);
  int count = BLE.scan(scanResults, SCAN_RESULT_MAX);
  for (int i = 0; i < count; i++)
  {
    uint8_t buf[BLE_MAX_ADV_DATA_LEN];
    size_t len;

    len = scanResults[i].advertisingData.get(BleAdvertisingDataType::MANUFACTURER_SPECIFIC_DATA, buf, BLE_MAX_ADV_DATA_LEN);
    if (buf[0] == 0xff && buf[1] == 0xff && buf[2] == 0x55)
    {
      uint8_t strLen = buf[3];
      char state[strLen];
      memcpy(&state, &buf[4], strLen);
      state[strLen] = '\0';

      Log.info("Received state of Length: %i", strLen);
      Log.info(state);
      if (!lastState.equals(state))
      {
        lastState = String(state);
        tft.fillRect(0, 60, 240, 320, HX8357_BLACK);
        tft.setTextSize(5);
        tft.setCursor(80, 100);
        tft.println(state);
      }
    }
  }
}