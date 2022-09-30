// Prova - Painel de Operador com Botão de Reset e Reinício de Ciclo
// Disciplina: Computational Thinking for Engineering (CTE)
// Aluno: Guilherme Macario da Silva - 1ECR

const int PIN_S1 = 2; // Sensor S1 (Entrada de peça)
const int PIN_S2 = 3; // Sensor S2 (Queda na caixa)
const int PIN_B1 = 4; // Botão de Reset B1
const int PIN_M1 = 8; // Motor M1 da Esteira
const int PIN_L1 = 9; // Lâmpada/LED L1 (Alerta de Caixa Cheia)

int contadorPecas = 0;

void setup() {
  pinMode(PIN_S1, INPUT_PULLUP);
  pinMode(PIN_S2, INPUT_PULLUP);
  pinMode(PIN_B1, INPUT_PULLUP);
  pinMode(PIN_M1, OUTPUT);
  pinMode(PIN_L1, OUTPUT);
  digitalWrite(PIN_M1, LOW);
  digitalWrite(PIN_L1, LOW);
  Serial.begin(9600);
}

void loop() {
  if (contadorPecas < 20) {
    if (digitalRead(PIN_S1) == LOW) {
      digitalWrite(PIN_M1, HIGH);
      while (digitalRead(PIN_S2) == HIGH) {
        delay(20);
      }
      contadorPecas++;
      Serial.print("Pecas processadas: ");
      Serial.println(contadorPecas);
      delay(200);
      
      if (contadorPecas >= 20) {
        digitalWrite(PIN_M1, LOW);
        digitalWrite(PIN_L1, HIGH); // Alerta operador
        Serial.println("Caixa cheia! Aguardando operador pressionar B1 (Reset)...");
      }
    }
  } else {
    // Aguarda operador pressionar botão de reset B1
    if (digitalRead(PIN_B1) == LOW) {
      delay(50); // Debounce
      if (digitalRead(PIN_B1) == LOW) {
        contadorPecas = 0;
        digitalWrite(PIN_L1, LOW);
        Serial.println("Ciclo reiniciado com sucesso.");
        while (digitalRead(PIN_B1) == LOW); // Espera soltar
      }
    }
  }
}
