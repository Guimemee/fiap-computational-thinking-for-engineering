# Projeto 1: Média de 5 Notas via Monitor Serial

> 1-) Faça um programa em C++ para Arduino que receba pela porta Serial o valor de 5 notas de avaliações (dígitos de 0 a 9), converta os caracteres ASCII recebidos para números inteiros, calcule a média aritmética em ponto flutuante e imprima o resultado formatado no Monitor Serial.

### Link do Código:
- 🔗 [`Projeto_01_Media_Notas_Serial.ino`](./Projeto_01_Media_Notas_Serial.ino)

### Resolução:
```cpp
// Projeto 1: Leitura Serial de 5 Notas e Cálculo de Média
int N1, N2, N3, N4, N5;
float M;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Digite o valor da Nota 1 (0 a 9):");
  while (Serial.available() == 0);
  N1 = Serial.read() - '0';
  
  Serial.println("Digite o valor da Nota 2 (0 a 9):");
  while (Serial.available() == 0);
  N2 = Serial.read() - '0';
  
  Serial.println("Digite o valor da Nota 3 (0 a 9):");
  while (Serial.available() == 0);
  N3 = Serial.read() - '0';
  
  Serial.println("Digite o valor da Nota 4 (0 a 9):");
  while (Serial.available() == 0);
  N4 = Serial.read() - '0';
  
  Serial.println("Digite o valor da Nota 5 (0 a 9):");
  while (Serial.available() == 0);
  N5 = Serial.read() - '0';
  
  M = (N1 + N2 + N3 + N4 + N5) / 5.0;
  
  Serial.print("Média Calculada: ");
  Serial.println(M);
  
  while(1); // Encerra o ciclo
}
```
