// Projeto 7: Sensor Ultrassônico de Distância HC-SR04 com Alarme Sonoro Buzzer
const int PIN_TRIG = 12;
const int PIN_ECHO = 13;
const int PIN_BUZZER = 11;
const int DISTANCIA_LIMITE = 20; // cm

void setup() {
  Serial.begin(9600);
  pinMode(PIN_TRIG, OUTPUT);
  pinMode(PIN_ECHO, INPUT);
  pinMode(PIN_BUZZER, OUTPUT);
}

void loop() {
  // Disparo do pulso de 10 microsegundos
  digitalWrite(PIN_TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(PIN_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIG, LOW);
  
  // Medição do tempo de retorno do eco
  long duracao = pulseIn(PIN_ECHO, HIGH);
  // Cálculo da distância em cm: (tempo * velocidade do som 0.0343 cm/us) / 2
  float distancia = (duracao * 0.0343) / 2.0;
  
  Serial.print("Distância Medida: ");
  Serial.print(distancia);
  Serial.println(" cm");
  
  if (distancia > 0 && distancia <= DISTANCIA_LIMITE) {
    tone(PIN_BUZZER, 1000); // Emite tom de 1kHz
    Serial.println(">> ALERTA: Proximidade crítica!");
  } else {
    noTone(PIN_BUZZER);     // Silencia buzzer
  }
  
  delay(100);
}
