// Display Setup
#include <Wire.h> 
#include <SFE_MicroOLED.h>  
#define PIN_RESET 9  
#define PIN_DC    8 
#define PIN_CS    10 
#define DC_JUMPER 1

MicroOLED oled(PIN_RESET, DC_JUMPER); 

// Communication Setup
#include <SoftwareSerial.h>  
int bluetoothTx = 3;  // TX-O 
int bluetoothRx = 2;  // RX-I 

SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);


void setup(){
  // Display
  oled.begin();
  oled.clear(PAGE);
  oled.clear(ALL);  

  //Bluetooth
  Serial.begin(9600); 
  bluetooth.begin(115200);  
  bluetooth.print("$");  // Print three times individually
  bluetooth.print("$");
  bluetooth.print("$");  // Enter command mode
  delay(100);  
  bluetooth.println("U,9600,N");  // Temporarily Change the baudrate to 9600, no parity
  bluetooth.begin(9600);
}

void loop(){
    if(bluetooth.available()){
      Serial.print((char)bluetooth.read());  
      oled.print((char)bluetooth.read()); 
   }
 }
