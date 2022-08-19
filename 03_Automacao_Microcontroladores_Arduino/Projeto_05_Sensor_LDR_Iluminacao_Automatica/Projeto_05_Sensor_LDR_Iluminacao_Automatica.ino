// Projeto 5: Iluminação Pública Inteligente com Sensor LDR Fotoresistor
const int PINO_LDR = A1;       // Entrada analógica do divisor de tensão com LDR
const int PINO_RELE_LED = 8;   // Saída digital de controle da lâmpada
const int LIMIAR_LUZ = 500;    // Ponto de corte para detecção de noite/escuro

void setup() {
  Serial.begin(9600);
  pinMode(PINO_RELE_LED, OUTPUT);
}

void loop() {
  int nivel_luz = analogRead(PINO_LDR);
  
  Serial.print("Luminosidade Ambiente: ");
  Serial.println(nivel_luz);
  
  if (nivel_luz < LIMIAR_LUZ) {
    digitalWrite(PINO_RELE_LED, HIGH); // Ambiente escuro: acende a luz
    Serial.println(">> Status: NOITE detectada - Lâmpada LIGADA");
  } else {
    digitalWrite(PINO_RELE_LED, LOW);  // Ambiente claro: apaga a luz
    Serial.println(">> Status: DIA detectado - Lâmpada DESLIGADA");
  }
  
  delay(1000);
}
