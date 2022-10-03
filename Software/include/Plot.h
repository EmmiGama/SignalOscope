#ifndef Plot_h
#define Plot_h

#include <Arduino.h>

#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SW 128
#define SH 64

#define OLED_RESET -1
Adafruit_SSD1306 _oled(SW, SH, &Wire, OLED_RESET);

class Plot {
  public:
    Plot();
    

  private:
    void graph(float xinf, float xsup, float yinf, float ysup);

};

Plot::Plot() {
  Wire.begin();
  _oled.begin(SSD1306_SWITCHCAPVCC, 0x3C);
}

void Plot::graph(float xinf, float xsup, float yinf, float ysup) {
  _oled.clearDisplay();
  _oled.setTextColor(SSD1306_WHITE);
  _oled.setCursor(x, y);
  _oled.setTextSize(6);
  _oled.print(s);
  _oled.display();

}

#endif