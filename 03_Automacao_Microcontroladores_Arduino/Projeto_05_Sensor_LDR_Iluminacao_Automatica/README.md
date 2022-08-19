# Projeto 5: Iluminação Pública Inteligente com Sensor LDR

> 5-) Projetar um sistema de poste inteligente (relé fotoelétrico) para acionamento automático de iluminação.
> - Conectar um fotoresistor LDR em configuração de divisor de tensão à porta analógica `A1`.
> - Quando a luminosidade for inferior a 500 unidades analógicas (ambiente noturno), ligar a lâmpada no pino digital `D8`.
> - Caso a luminosidade seja superior ou igual a 500 unidades, desligar o circuito e registrar a telemetria na porta serial a cada 1 segundo.

### Link do Código:
- 🔗 [`Projeto_05_Sensor_LDR_Iluminacao_Automatica.ino`](./Projeto_05_Sensor_LDR_Iluminacao_Automatica.ino)

### Resolução:
```cpp
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
```
