int inputPin = D9;              // choose the input pin (for PIR sensor)
int ledPin = D3;                // LED Pin
int pirState = LOW;             // we start, assuming no motion detected
int val = 0;                    // variable for reading the pin status

int calibrateTime = 5000;      // wait for the thingy to calibrate

void setup() {
    pinMode(ledPin, OUTPUT);
    pinMode(inputPin, INPUT);     // declare sensor as input
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
        // announce this change by publishing an event
        if (pirState == LOW) {
          // we have just turned on
          Particle.publish("motion", "1" , PRIVATE);
          // Update the current state
          pirState = HIGH;
          setLED(pirState);
        }
          } else {
        if (pirState == HIGH) {
          // we have just turned of
          // Update the current state
          Particle.publish("motion", "0", PRIVATE);
          pirState = LOW;
          setLED(pirState);
        }
    }
}
