int inputPin = D9;     // input pin (for PIR sensor)
int ledPin = D3;       // LED Pin
int pirState = LOW;    // Assumption of no movement
int val = 0;           

int calibrateTime = 3000;      // waitinng for calibration

void setup() {
    pinMode(ledPin, OUTPUT);
    pinMode(inputPin, INPUT);     
}

void loop() {
  
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
        if (pirState == LOW) {
          // we have just turned on
          Particle.publish("motion", "1" , PRIVATE);
          // Update the current state
          pirState = HIGH;
          setLED(pirState);
        }
          } else {
        if (pirState == HIGH) {
          // turned off
          // Update on current state
          Particle.publish("motion", "0", PRIVATE);
          pirState = LOW;
          setLED(pirState);
        }
    }
}
