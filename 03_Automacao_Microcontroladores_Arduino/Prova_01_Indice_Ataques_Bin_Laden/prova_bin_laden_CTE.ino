// Prova Prática Arduino C: Cálculo do Índice de Eminência de Novos Ataques Terroristas (Bin Laden)
// Instituição: FIAP • Curso: Engenharia da Computação • Turma: 1ECR • Data: 08/05/2019
// Disciplina: Computational Thinking for Engineering (CTE) • Professor: Fabio H. Pimentel
// Aluno: Guilherme Macario da Silva • RM: 84053

#include <math.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);
  Serial.println("==================================================");
  Serial.println("SISTEMA DE CALCULO DE RISCO DE ATAQUES TERRORISTAS");
  Serial.println("==================================================");
}

void loop() {
  int ano = 0;
  int mes = 0;
  float indice = 0.0;

  Serial.println("\nDigite o ANO (4 digitos, ex: 2011): ");
  while (Serial.available() == 0);
  ano = Serial.parseInt();

  Serial.println("Digite o MES (1 a 12, ex: 05): ");
  while (Serial.available() == 0);
  mes = Serial.parseInt();

  Serial.print("Data informada: ");
  if (mes < 10) Serial.print("0");
  Serial.print(mes);
  Serial.print("/");
  Serial.println(ano);

  // Regra de Negócio da Avaliação:
  // Até e durante maio/2011 (mes <= 5 e ano <= 2011): Indice = sqrt(ano) + mes^3
  // Após maio/2011: Indice = (ano / 2.0) - mes^2
  if (ano < 2011 || (ano == 2011 && mes <= 5)) {
    indice = sqrt((float)ano) + pow((float)mes, 3);
    Serial.println("Criterio: Ate maio/2011 -> sqrt(ano) + mes^3");
  } else {
    indice = (ano / 2.0) - pow((float)mes, 2);
    Serial.println("Criterio: Apos maio/2011 -> (ano / 2) - mes^2");
  }

  Serial.print("Indice de Eminencia de Novos Ataques: ");
  Serial.println(indice, 2);
  Serial.println("--------------------------------------------------");
  delay(2000);
}
