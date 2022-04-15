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
