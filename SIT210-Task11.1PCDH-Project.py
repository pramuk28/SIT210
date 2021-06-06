#define MOVEMENT_THRESHOLD 100

int inputPin = D9;     // input pin (for PIR sensor/movement)
int ledPin = D3;       // LED Pin
int movement = LOW;    // Assumption of no movement
int val = 0;           

int calibrateTime = 3000;      // waitinng for calibration

void setup() {
    pinMode(ledPin, OUTPUT);
    pinMode(inputPin, INPUT);     
}
void loop() {
    
    int movement = random(8,12)*100;
  
  // if the sensor is calibrated
  if (calibrated()) {
      
  // get the data from the sensor
    readTheSensor();
    
    // report it out, if the state has changed
    reportTheData();
    }
}
void readTheSensor() {
    val = digitalRead(inputPin);
}
bool calibrated() {
    return millis() - calibrateTime > 0;
}
void setLED(int state) {
    digitalWrite(ledPin, state);
}
void reportTheData() {
    if (val == HIGH) {
        // the current state is no motion
        // i.e. it's just changed
        // Publishing an event to notify the owner
        if (movement == LOW) {
          // we have just turned on
          Particle.publish("motion", "ACTIVE");
          // Update the current state
          movement = HIGH;
          setLED(movement);
        }
          } else {
        if (movement == HIGH) {
          // turned off
          // Update on current state
          Particle.publish("motion", "INACTIVE");
          movement = LOW;
          setLED(movement);
        }
    }
}
