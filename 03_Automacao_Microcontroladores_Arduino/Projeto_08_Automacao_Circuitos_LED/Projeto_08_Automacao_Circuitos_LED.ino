// Projeto 08: Automação de Circuitos e Controle de LEDs com Arduino (C++)
// Acionamento de atuadores e sinalizadores luminosos

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(500);
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
}
