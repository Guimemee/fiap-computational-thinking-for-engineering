// Prova Prática Arduino C: Sistema Eletrônico Sinalizador de Ambulância (SAMU)
// Instituição: FIAP • Curso: Engenharia da Computação • Turma: 1ECR
// Disciplina: Computational Thinking for Engineering (CTE) • Professor: Fabio H. Pimentel
// Aluno: Guilherme Macario da Silva • RM: 84053

// Definição de Pinos das Chaves
const int CH1 = 8;   // Chave 1 (Prioridade Máxima de Emergência)
const int CH2 = 9;   // Chave 2 (Sinalizador Estroboscópico LEDs 4 e 5)
const int CH3 = 10;  // Chave 3 (Sinalizador de Posição LED 1 e LED 2)

// Definição de Pinos dos LEDs
const int LED1 = 3;  // LED 1 (Pisca 1s aceso / 2s apagado quando CH3 = ON)
const int LED2 = 4;  // LED 2 (Aceso contínuo quando CH3 = OFF)
const int LED3 = 5;  // LED 3 (Prioridade de Emergência: Aceso contínuo quando CH1 = ON)
const int LED4 = 6;  // LED 4 (Pisca complementar 2s com LED 5 quando CH2 = ON)
const int LED5 = 7;  // LED 5 (Pisca complementar 2s com LED 4 quando CH2 = ON)

void setup() {
  pinMode(CH1, INPUT);
  pinMode(CH2, INPUT);
  pinMode(CH3, INPUT);

  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);
  pinMode(LED5, OUTPUT);
}

void loop() {
  int estadoCh1 = digitalRead(CH1);
  int estadoCh2 = digitalRead(CH2);
  int estadoCh3 = digitalRead(CH3);

  // CHAVE 1 (Prioridade Máxima):
  // Quando em ON: Desabilita chaves 2 e 3, acende continuamente LED 3 e apaga os demais LEDs.
  if (estadoCh1 == HIGH) {
    digitalWrite(LED3, HIGH);
    digitalWrite(LED1, LOW);
    digitalWrite(LED2, LOW);
    digitalWrite(LED4, LOW);
    digitalWrite(LED5, LOW);
  } else {
    // Quando em OFF: Libera as funções das chaves 2 e 3, e apaga o LED 3.
    digitalWrite(LED3, LOW);

    // Controle da Chave 2 (LEDs 4 e 5 complementares em intervalos de 2 segundos)
    if (estadoCh2 == HIGH) {
      digitalWrite(LED4, HIGH);
      digitalWrite(LED5, LOW);
      delay(2000);
      digitalWrite(LED4, LOW);
      digitalWrite(LED5, HIGH);
      delay(2000);
    } else {
      digitalWrite(LED4, LOW);
      digitalWrite(LED5, LOW);
    }

    // Controle da Chave 3:
    // ON  -> Liga LED 1 (1s aceso / 2s apagado periodicamente) e desliga LED 2
    // OFF -> Liga LED 2 com acendimento contínuo e desliga LED 1
    if (estadoCh3 == HIGH) {
      digitalWrite(LED2, LOW);
      digitalWrite(LED1, HIGH);
      delay(1000);
      digitalWrite(LED1, LOW);
      delay(2000);
    } else {
      digitalWrite(LED1, LOW);
      digitalWrite(LED2, HIGH);
    }
  }
}
