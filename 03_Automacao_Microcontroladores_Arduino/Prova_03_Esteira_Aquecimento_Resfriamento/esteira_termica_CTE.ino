// Prova - Automação de Esteira Industrial com Aquecimento e Resfriamento
// Disciplina: Computational Thinking for Engineering (CTE)
// Aluno: Guilherme Macario da Silva - 1ECR

const int PIN_S1 = 2; // Sensor S1 (Presença inicial)
const int PIN_S2 = 3; // Sensor S2 (Aquecedor)
const int PIN_S3 = 4; // Sensor S3 (Resfriador)
const int PIN_S4 = 5; // Sensor S4 (Saída)
const int PIN_M1 = 8; // Motor M1 da Esteira

void setup() {
  pinMode(PIN_S1, INPUT_PULLUP);
  pinMode(PIN_S2, INPUT_PULLUP);
  pinMode(PIN_S3, INPUT_PULLUP);
  pinMode(PIN_S4, INPUT_PULLUP);
  pinMode(PIN_M1, OUTPUT);
  digitalWrite(PIN_M1, LOW);
  Serial.begin(9600);
}

void aguardarSensor(int pin) {
  while (digitalRead(pin) == HIGH) {
    delay(20);
  }
}

void loop() {
  aguardarSensor(PIN_S1);
  digitalWrite(PIN_M1, HIGH);
  
  aguardarSensor(PIN_S2);
  digitalWrite(PIN_M1, LOW);
  delay(3000); // Aguarda 3 segundos no aquecimento
  
  digitalWrite(PIN_M1, HIGH);
  aguardarSensor(PIN_S3);
  digitalWrite(PIN_M1, LOW);
  delay(4000); // Aguarda 4 segundos no resfriamento
  
  digitalWrite(PIN_M1, HIGH);
  aguardarSensor(PIN_S4);
  digitalWrite(PIN_M1, LOW); // Finaliza ciclo e desliga o motor
}
