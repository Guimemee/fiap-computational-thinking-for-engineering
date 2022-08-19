# Projeto 6: Contador Decimal 0 a 9 em Display de 7 Segmentos

> 6-) Desenvolver o acionamento de um display numérico de 7 segmentos (catodo comum) para exibir a contagem progressiva de 0 a 9 com repetição infinita.
> - Mapear os segmentos `a` até `g` nos pinos digitais `2` a `8`.
> - Utilizar matriz de estados booleanos (`byte digitos[10][7]`) para sintetizar cada número decimal.
> - Intervalo de transição fixado em 1 segundo por caractere.

### Link do Código:
- 🔗 [`Projeto_06_Display_7_Segmentos_Contador.ino`](./Projeto_06_Display_7_Segmentos_Contador.ino)

### Resolução:
```cpp
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
```
