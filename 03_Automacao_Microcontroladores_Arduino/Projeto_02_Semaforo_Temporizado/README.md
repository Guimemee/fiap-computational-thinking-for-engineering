# Projeto 2: Semáforo Automático Temporizado

> 2-) Implementar o controle de um semáforo veicular padrão de três tempos utilizando as saídas digitais do Arduino (Pinos 8, 9 e 10).
> - Verde: ligado por 5 segundos.
> - Amarelo: ligado por 2 segundos.
> - Vermelho: ligado por 5 segundos.

### Link do Código:
- 🔗 [`Projeto_02_Semaforo_Temporizado.ino`](./Projeto_02_Semaforo_Temporizado.ino)

### Resolução:
```cpp
// Projeto 2: Semáforo Automático Temporizado
const int LED_VERMELHO = 10;
const int LED_AMARELO = 9;
const int LED_VERDE = 8;

void setup() {
  pinMode(LED_VERMELHO, OUTPUT);
  pinMode(LED_AMARELO, OUTPUT);
  pinMode(LED_VERDE, OUTPUT);
}

void loop() {
  // Fase 1: Verde (5 segundos)
  digitalWrite(LED_VERDE, HIGH);
  digitalWrite(LED_AMARELO, LOW);
  digitalWrite(LED_VERMELHO, LOW);
  delay(5000);
  
  // Fase 2: Amarelo (2 segundos)
  digitalWrite(LED_VERDE, LOW);
  digitalWrite(LED_AMARELO, HIGH);
  digitalWrite(LED_VERMELHO, LOW);
  delay(2000);
  
  // Fase 3: Vermelho (5 segundos)
  digitalWrite(LED_VERDE, LOW);
  digitalWrite(LED_AMARELO, LOW);
  digitalWrite(LED_VERMELHO, HIGH);
  delay(5000);
}
```
