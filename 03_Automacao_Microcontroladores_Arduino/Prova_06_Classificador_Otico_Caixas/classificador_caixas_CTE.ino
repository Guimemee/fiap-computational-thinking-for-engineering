// Prova - Classificador Ótico de Caixas por Altura com Sensores Múltiplos
// Disciplina: Computational Thinking for Engineering (CTE)
// Aluno: Guilherme Macario da Silva - 1ECR

const int PIN_S1 = 2; // Sensor S1 (Entrada da caixa)
const int PIN_S2 = 3; // Sensor S2 (Altura Baixa)
const int PIN_S3 = 4; // Sensor S3 (Altura Média)
const int PIN_S4 = 5; // Sensor S4 (Altura Alta)
const int PIN_S5 = 6; // Sensor S5 (Fim da esteira)

const int PIN_M1 = 8;  // Motor M1
const int PIN_L1 = 9;  // LED L1 (Caixa Baixa)
const int PIN_L2 = 10; // LED L2 (Caixa Média)
const int PIN_L3 = 11; // LED L3 (Caixa Alta)

void setup() {
  pinMode(PIN_S1, INPUT_PULLUP);
  pinMode(PIN_S2, INPUT_PULLUP);
  pinMode(PIN_S3, INPUT_PULLUP);
  pinMode(PIN_S4, INPUT_PULLUP);
  pinMode(PIN_S5, INPUT_PULLUP);
  
  pinMode(PIN_M1, OUTPUT);
  pinMode(PIN_L1, OUTPUT);
  pinMode(PIN_L2, OUTPUT);
  pinMode(PIN_L3, OUTPUT);
  
  digitalWrite(PIN_M1, LOW);
  apagarLEDs();
  Serial.begin(9600);
}

void apagarLEDs() {
  digitalWrite(PIN_L1, LOW);
  digitalWrite(PIN_L2, LOW);
  digitalWrite(PIN_L3, LOW);
}

void loop() {
  apagarLEDs();
  while (digitalRead(PIN_S1) == HIGH) {
    delay(20);
  }
  
  digitalWrite(PIN_M1, HIGH);
  delay(100);
  
  // Classificação pela altura dos sensores
  if (digitalRead(PIN_S4) == LOW) {
    digitalWrite(PIN_L3, HIGH); // Caixa Alta
    Serial.println("Caixa Alta detectada (L3)");
  } else if (digitalRead(PIN_S3) == LOW) {
    digitalWrite(PIN_L2, HIGH); // Caixa Média
    Serial.println("Caixa Media detectada (L2)");
  } else {
    digitalWrite(PIN_L1, HIGH); // Caixa Baixa
    Serial.println("Caixa Baixa detectada (L1)");
  }
  
  while (digitalRead(PIN_S5) == HIGH) {
    delay(20);
  }
  digitalWrite(PIN_M1, LOW);
  apagarLEDs();
}
