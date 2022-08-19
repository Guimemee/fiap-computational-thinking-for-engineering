# Projeto 7: Sensor Ultrassônico de Distância e Alarme com Buzzer

> 7-) Implementar um radar de proximidade veicular / industrial utilizando o sensor ultrassônico HC-SR04 e um buzzer piezoelétrico.
> - Emitir pulso de Trigger no pino `D12` por 10µs e medir o tempo de reflexão do Echo no pino `D13`.
> - Calcular a distância física real utilizando a velocidade do som no ar.
> - Se a distância for menor ou igual a 20 cm, disparar alarme sonoro contínuo no buzzer (`D11`) e alertar na saída Serial.

### Link do Código:
- 🔗 [`Projeto_07_Sensor_Ultrassonico_Alarme_Buzzer.ino`](./Projeto_07_Sensor_Ultrassonico_Alarme_Buzzer.ino)

### Resolução:
```cpp
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
```
