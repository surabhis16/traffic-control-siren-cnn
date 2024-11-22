#include <Wire.h>
#include <LiquidCrystal_I2C.h>

const int redLedPin = 13;
const int greenLedPin = 5;
unsigned long previousMillis = 0;
const long interval = 90000;  // 90 seconds in milliseconds
bool isRedOn = true;
String lastCommand = "";

// Set the LCD address to 0x27 for a 16x2 display
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);
  pinMode(redLedPin, OUTPUT);
  pinMode(greenLedPin, OUTPUT);
  digitalWrite(redLedPin, HIGH);  // Start with the red LED on
  digitalWrite(greenLedPin, LOW);

  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Timer: 90 secs");
}

void loop() {
  unsigned long currentMillis = millis();

  // Check for serial input
  if (Serial.available() > 0) {
    String msg = Serial.readStringUntil('\n');
    msg.trim();

    if (msg == "ambulance" && isRedOn) {
      digitalWrite(redLedPin, LOW);  // Turn off the red LED
      digitalWrite(greenLedPin, HIGH);  // Turn on the green LED
      lcd.clear();
      lcd.setCursor(0, 1);
      lcd.print("Ambulance    ");
      delay(5000);  // Keep the green LED on for 5 seconds
      digitalWrite(greenLedPin, LOW);
      digitalWrite(redLedPin, HIGH);  // Turn the red LED back on
      previousMillis = currentMillis;  // Reset the timer
      isRedOn = true;
      lastCommand = "ambulance";
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Timer: 90 secs");
    } else if (msg == "notambulance") {
      lastCommand = "notambulance";
    }

    // Update the LCD with the current message
    if (lastCommand == "notambulance") {
      lcd.setCursor(0, 1);
      lcd.print("Not Ambulance");
    }
  }

  // Timer logic
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    isRedOn = !isRedOn;

    if (isRedOn) {
      digitalWrite(redLedPin, HIGH);
      digitalWrite(greenLedPin, LOW);
    } else {
      digitalWrite(redLedPin, LOW);
      digitalWrite(greenLedPin, HIGH);
    }
  }

  // Display the remaining time on the LCD only if not in "ambulance" state
  if (lastCommand != "ambulance") {
    int remainingTime = (interval - (currentMillis - previousMillis)) / 1000;
    lcd.setCursor(7, 0);
    lcd.print(remainingTime);
    lcd.print(" secs   ");
  }
}



