// Projeto 4: Controle de Intensidade Luminosa de LED via PWM e Potenciômetro
const int PINO_POT = A0;   // Entrada analógica do potenciômetro
const int PINO_LED = 9;    // Saída PWM conectada ao LED

void setup() {
  Serial.begin(9600);
  pinMode(PINO_LED, OUTPUT);
}

void loop() {
  int valor_pot = analogRead(PINO_POT);             // Leitura de 0 a 1023 (10 bits)
  int valor_pwm = map(valor_pot, 0, 1023, 0, 255);  // Escala para 8 bits (0 a 255)
  
  analogWrite(PINO_LED, valor_pwm);                 // Modulação por Largura de Pulso
  
  Serial.print("Leitura Potenciômetro: ");
  Serial.print(valor_pot);
  Serial.print(" | Sinal PWM Gerado: ");
  Serial.println(valor_pwm);
  
  delay(50);
}
