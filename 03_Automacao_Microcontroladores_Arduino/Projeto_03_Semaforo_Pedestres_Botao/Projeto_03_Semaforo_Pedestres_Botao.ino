// Projeto 3: Semáforo com Botão de Pedestre
const int CAR_RED = 12;
const int CAR_YELLOW = 11;
const int CAR_GREEN = 10;
const int PED_RED = 9;
const int PED_GREEN = 8;
const int BUTTON = 2;

void setup() {
  pinMode(CAR_RED, OUTPUT);
  pinMode(CAR_YELLOW, OUTPUT);
  pinMode(CAR_GREEN, OUTPUT);
  pinMode(PED_RED, OUTPUT);
  pinMode(PED_GREEN, OUTPUT);
  pinMode(BUTTON, INPUT_PULLUP);
}

void loop() {
  // Estado Normal: Carros Verde, Pedestres Vermelho
  digitalWrite(CAR_GREEN, HIGH);
  digitalWrite(CAR_YELLOW, LOW);
  digitalWrite(CAR_RED, LOW);
  digitalWrite(PED_GREEN, LOW);
  digitalWrite(PED_RED, HIGH);
  
  if (digitalRead(BUTTON) == LOW) { // Botão pressionado
    delay(1000); // Aguarda 1s
    
    // Transição Carros Amarelo
    digitalWrite(CAR_GREEN, LOW);
    digitalWrite(CAR_YELLOW, HIGH);
    delay(2000);
    
    // Carros Vermelho, Pedestres Verde
    digitalWrite(CAR_YELLOW, LOW);
    digitalWrite(CAR_RED, HIGH);
    digitalWrite(PED_RED, LOW);
    digitalWrite(PED_GREEN, HIGH);
    delay(5000); // 5s para atravessar
    
    // Alerta Pedestres (Pisca Vermelho)
    digitalWrite(PED_GREEN, LOW);
    for (int i = 0; i < 5; i++) {
      digitalWrite(PED_RED, HIGH);
      delay(250);
      digitalWrite(PED_RED, LOW);
      delay(250);
    }
  }
}
