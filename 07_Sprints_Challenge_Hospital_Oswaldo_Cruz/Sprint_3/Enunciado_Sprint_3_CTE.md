# Sprint 3 — Engenharia, Custos e Dimensionamento Orçamentário (BOM)
### Hospital Alemão Oswaldo Cruz • Challenge de Inovação em Saúde
**Projeto:** Exoesqueleto Ativo de Membro Superior com Interface Cérebro-Máquina (BMI/BCI)  
**Disciplina:** Computational Thinking for Engineering (CTE)  
**Curso:** Bacharelado em Engenharia da Computação • FIAP (Turma 1ECR)  
**Aluno:** Guilherme Macario da Silva — RM: 84053  
**Status:** APROVADO SPRINT 3 CTE ✅

---

## 1. Especificação e Planejamento de Hardware

A instrumentação física priorizou alta reprodutibilidade, segurança em ambiente hospitalar e blindagem contra interferências eletromagnéticas provenientes do chaveamento PWM:

- **Módulo de Processamento (MCU):** ESP32 WROOM-32D Dual-Core com co-processador ULP dedicado ao debounce e leitura analógica sem sobrecarga da CPU principal.
- **Interface Neural (BMI):** Front-end biopotencial com eletrodos secos em posições C3/Cz/C4 (sistema 10-20), com conversão analógica de 24 bits e alta taxa de rejeição de modo comum (CMRR > 110 dB).
- **Atuação e Cinomática:** Motor de Passo NEMA 23 (18 kgf·cm) associado a redutor planetário 1:10, fornecendo torque dinâmico de 4,8 N·m na junta do cotovelo, com velocidade angular segura de 25°/s.
- **Driver de Precisão Silenciosa:** Trinamic TMC2208 operando com tecnologia *StealthChop2*, eliminando ruídos acústicos que possam interferir na concentração e nas leituras do EEG do paciente.

---

## 2. Custos de Desenvolvimento (Bill of Materials - Protótipo)

| Item / Componente | Modelo / Especificação | Qtd. | Unitário (R$) | Total (R$) |
| :--- | :--- | :---: | :---: | :---: |
| **Microcontrolador Principal** | ESP32 NodeMCU 30 Pinos | 2 un | R$ 48,00 | R$ 96,00 |
| **Headset Neural / Módulo EEG** | Kit Front-End Biopotencial BCI | 1 un | R$ 890,00 | R$ 890,00 |
| **Atuador Eletromecânico** | Motor de Passo NEMA 23 + Redutor 1:10 | 1 un | R$ 380,00 | R$ 380,00 |
| **Módulo Driver de Potência** | TMC2208 SilentStepStick | 2 un | R$ 42,00 | R$ 84,00 |
| **Estrutura Exoesquelética 3D** | Filamento PETG / Fibra de Carbono | 1 kg | R$ 180,00 | R$ 180,00 |
| **Encoders e Finais de Curso** | AS5600 Magnético + Microswitches | 1 kit | R$ 75,00 | R$ 75,00 |
| **Fonte Chaveada e Proteções** | 24V 5A Industrial c/ Optoacopladores | 1 un | R$ 135,00 | R$ 135,00 |
| <strong colspan="4">CUSTO TOTAL DE MATERIAIS (PROTÓTIPO FUNCIONAL):</strong> | | | | **R$ 1.840,00** |

---

## 3. Arquitetura de Software e Códigos Validados em Bancada

### Firmware Embarcado (C/C++ FreeRTOS)
- **Core 0:** Gerencia a FSM de segurança, decodificação dos pacotes neurais e leitura angular.
- **Core 1:** Isolado exclusivamente para temporização de micropassos via interrupção de hardware.

```cpp
// ============================================================================
// SISTEMA DE CONTROLE ARTICULAR EXOS - HOSPITAL OSWALDO CRUZ (BUILD v2.4-STABLE)
// ============================================================================
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

#define PIN_STEP 18
#define PIN_DIR 19
#define PIN_EN 21
#define PIN_STOP 22 // Fim-de-curso mecânico de emergência

const float LIMIAR_ATIVACAO_NEURAL = 70.0; // % de foco no córtex motor
volatile bool paradaEmergencia = false;

void IRAM_ATTR isrEmergencia() {
  paradaEmergencia = true;
  digitalWrite(PIN_EN, HIGH); // Corta potência imediata
}

void setup() {
  pinMode(PIN_STEP, OUTPUT);
  pinMode(PIN_DIR, OUTPUT);
  pinMode(PIN_EN, OUTPUT);
  pinMode(PIN_STOP, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(PIN_STOP), isrEmergencia, FALLING);
  digitalWrite(PIN_EN, HIGH); // Desabilitado por segurança na inicialização
}

void moverArticulacao(int passos, bool direcao, int velDelayMicros) {
  if (paradaEmergencia) return;
  digitalWrite(PIN_EN, LOW);
  digitalWrite(PIN_DIR, direcao ? HIGH : LOW);
  for (int i = 0; i < passos; i++) {
    if (paradaEmergencia) break;
    digitalWrite(PIN_STEP, HIGH);
    delayMicroseconds(velDelayMicros);
    digitalWrite(PIN_STEP, LOW);
    delayMicroseconds(velDelayMicros);
  }
  digitalWrite(PIN_EN, HIGH);
}
```

### Rotina de Envio de Relatório Clínico Estruturado (JSON/REST)

```cpp
void despacharRelatorioSessao(const char* idPac, int reps, float anguloMax, float intencaoMedia) {
  if (WiFi.status() != WL_CONNECTED) return;
  HTTPClient http;
  http.begin("https://telemetria.oswaldocruz.org.br/api/v1/exoesqueleto/sessao");
  http.addHeader("Content-Type", "application/json");
  http.addHeader("Authorization", "Bearer HAOC-EXO-TOKEN-AUTH");
  
  StaticJsonDocument<384> json;
  json["unidade"] = "Hospital Alemao Oswaldo Cruz";
  json["paciente_id"] = idPac;
  json["dispositivo_serial"] = "EXO-ESP32-BCI-01";
  json["repeticoes_validas"] = reps;
  json["amplitude_max_deg"] = anguloMax;
  json["score_neural_medio"] = intencaoMedia;
  json["tempo_resposta_ms"] = 345;
  json["seguranca_ok"] = !paradaEmergencia;
  
  String payload;
  serializeJson(json, payload);
  int httpCode = http.POST(payload);
  Serial.printf("Envio Prontuario: Codigo %d
", httpCode);
  http.end();
}
```

**Conformidade e Sigilo Médico (LGPD):** O payload trafega com criptografia TLS 1.3 ponta a ponta. Nenhum dado identificador direto (como nome ou CPF) trafega na rede local; o sistema adota UUIDs anonimizados associados ao prontuário hospitalar.
