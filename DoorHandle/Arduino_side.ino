void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ;
  }
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    
    if (data.length() > 0) {
      Serial.print("Receive: ");
      Serial.println(data);
    }

    if(data == "LOCK"){
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1111);
      digitalWrite(LED_BUILTIN, LOW);

    }

    if(data == "UNLOCK"){
      digitalWrite(LED_BUILTIN, HIGH);
      delay(2222);
      digitalWrite(LED_BUILTIN, LOW);

    }

    if (data.startsWith("LOCKTOUCH,")) {
      String delayValueStr = data.substring(10);
      int delayValue = delayValueStr.toInt();
      
      if (delayValue > 0) {
        Serial.print("LOCKTOUCH delay: ");
        Serial.println(delayValue);
        digitalWrite(LED_BUILTIN, HIGH);
        delay(delayValue);
        digitalWrite(LED_BUILTIN, LOW);
      } else {
        Serial.println("Invalid LOCKTOUCH value");
      }
    }

    if (data.startsWith("UNLOCKTOUCH,")) {
      String delayValueStr = data.substring(12);
      int delayValue = delayValueStr.toInt();
      
      if (delayValue > 0) {
        Serial.print("UNLOCKTOUCH delay: ");
        Serial.println(delayValue);
        digitalWrite(LED_BUILTIN, HIGH);
        delay(delayValue);
        digitalWrite(LED_BUILTIN, LOW);
      } else {
        Serial.println("Invalid UNLOCKTOUCH value");
      }
    }
  }
}

