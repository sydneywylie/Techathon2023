#include <math.h>
const int a = a;
const int b = 2;
const int c = 4;
float temperature;
int B=3975;                  //B value of the thermistor
float resistance;
float sensorReading;
float sensorData;
int data; 
 
void setup()
{
    Serial.begin(9600);
    pinMode(b, INPUT);
    pinMode(c, OUTPUT);
}
 
void loop()
{
    sensorData=analogRead(a);
    resistance=(float)(1023-sensorData)*10000/sensorData; //get the resistance of the sensor;
    temperature=1/(log(resistance/10000)/B+1/298.15)-273.15;//convert to temperature via datasheet&nbsp;;
    delay(1000);
    Serial.print(temperature);
    Serial.print(" ");
    
    int sensorReading=digitalRead(b);
    Serial.print(sensorReading);
    Serial.println();

  
    if(sensorReading==1)
    {
        digitalWrite(c,HIGH);
    }
    else
    {
        digitalWrite(c,LOW);
    }

     // see if there's incoming serial data:
  while (Serial.available())
  {
    data = Serial.read();
  }

  if (data == '1')
  digitalWrite (c, HIGH);

  else if (data == '0')
  digitalWrite (c, LOW);
  
} 