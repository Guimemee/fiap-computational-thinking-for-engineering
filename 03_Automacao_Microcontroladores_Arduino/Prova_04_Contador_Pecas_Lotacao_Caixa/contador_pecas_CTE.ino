// Prova - Contador de Peças Industriais com Alerta de Lotação de Caixa
// Disciplina: Computational Thinking for Engineering (CTE)
// Aluno: Guilherme Macario da Silva - 1ECR

const int PIN_S1 = 2; // Sensor S1 (Entrada de peça)
const int PIN_S2 = 3; // Sensor S2 (Queda na caixa)
const int PIN_M1 = 8; // Motor M1 da Esteira
const int PIN_L1 = 9; // Lâmpada/LED L1 (Alerta de Caixa Cheia)

int totalPecas = 0;

void setup() {
  pinMode(PIN_S1, INPUT_PULLUP);
  pinMode(PIN_S2, INPUT_PULLUP);
  pinMode(PIN_M1, OUTPUT);
  pinMode(PIN_L1, OUTPUT);
  digitalWrite(PIN_M1, LOW);
  digitalWrite(PIN_L1, LOW);
  Serial.begin(9600);
}

void loop() {
  if (totalPecas < 20) {
    if (digitalRead(PIN_S1) == LOW) {
      digitalWrite(PIN_M1, HIGH);
      while (digitalRead(PIN_S2) == HIGH) {
        delay(20);
      }
      totalPecas++;
      Serial.print("Pecas na caixa: ");
      Serial.println(totalPecas);
      delay(200);
      
      if (totalPecas >= 20) {
        digitalWrite(PIN_M1, LOW);
        digitalWrite(PIN_L1, HIGH); // Alerta de caixa lotada
        Serial.println("ALERTA: Caixa lotada (20 pecas). Substitua a caixa!");
      }
    }
  }
}
