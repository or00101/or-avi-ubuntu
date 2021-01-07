#define LED 8
//#define IN 8
#define BAUD_RATE 9600

int state = 0;

void setup() {
  pinMode(LED, OUTPUT);
  //pinMode(IN, INPUT);
  Serial.begin(BAUD_RATE);
}

void loop() {
  //int state = digitalRead(IN);
  int ser_in = Serial.read();
  
  if (ser_in != -1 && ser_in != 10){
    state = ser_in - '0';
    Serial.println(state);
  }

  if (state == 1){
    digitalWrite(LED, HIGH);
  }
  else{
    digitalWrite(LED, LOW);
  }
}
