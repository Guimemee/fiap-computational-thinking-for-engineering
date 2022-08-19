// Projeto 6: Contador Decimal de 0 a 9 em Display de 7 Segmentos Catodo Comum
// Mapeamento dos segmentos: a, b, c, d, e, f, g -> pinos 2 a 8
const int pinos_segmentos[7] = {2, 3, 4, 5, 6, 7, 8};

// Tabela verdade dos dígitos 0 a 9 (1 = aceso, 0 = apagado)
const byte digitos[10][7] = {
  {1, 1, 1, 1, 1, 1, 0}, // 0
  {0, 1, 1, 0, 0, 0, 0}, // 1
  {1, 1, 0, 1, 1, 0, 1}, // 2
  {1, 1, 1, 1, 0, 0, 1}, // 3
  {0, 1, 1, 0, 0, 1, 1}, // 4
  {1, 0, 1, 1, 0, 1, 1}, // 5
  {1, 0, 1, 1, 1, 1, 1}, // 6
  {1, 1, 1, 0, 0, 0, 0}, // 7
  {1, 1, 1, 1, 1, 1, 1}, // 8
  {1, 1, 1, 1, 0, 1, 1}  // 9
};

void setup() {
  for (int i = 0; i < 7; i++) {
    pinMode(pinos_segmentos[i], OUTPUT);
  }
}

void loop() {
  for (int num = 0; num <= 9; num++) {
    for (int seg = 0; seg < 7; seg++) {
      digitalWrite(pinos_segmentos[seg], digitos[num][seg]);
    }
    delay(1000); // 1 segundo por dígito
  }
}
