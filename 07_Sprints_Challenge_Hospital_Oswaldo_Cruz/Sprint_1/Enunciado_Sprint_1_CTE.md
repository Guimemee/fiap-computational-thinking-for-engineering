# Sprint 1 — Proposta do Challenge, Requisitos e Concepção Clínica
### Hospital Alemão Oswaldo Cruz • Challenge de Inovação em Saúde
**Projeto:** Exoesqueleto Ativo de Membro Superior com Interface Cérebro-Máquina (BMI/BCI)  
**Disciplina:** Computational Thinking for Engineering (CTE)  
**Curso:** Bacharelado em Engenharia da Computação • FIAP (Turma 1ECR)  
**Aluno:** Guilherme Macario da Silva — RM: 84053  
**Status:** CONCLUÍDO E VALIDADO ✅

---

## 1. Ideia Consolidada e Objetivo Clínico

### 🎯 Objetivo Central
Desenvolver um exoesqueleto robótico de membro superior assistido por **Interface Cérebro-Máquina (BMI/BCI)** não invasiva, microcontrolado via **ESP32**, visando a neurorreabilitação motora ativa de pacientes pós-Acidente Vascular Cerebral (AVC) e portadores de lesões neuromusculares no **Hospital Alemão Oswaldo Cruz**.

### 🔬 Fundamentação e Neuroplasticidade
A recuperação funcional tradicional frequentemente sofre com a dissociação temporal entre a intenção voluntária do paciente e a resposta mecânica do membro paralisado. Ao capturar os ritmos sensoriomotores (ondas Mu e Beta no córtex motor) momentos antes da execução, o exoesqueleto atua em regime de **assist-as-needed** (assistência sob demanda), potencializando a neuroplasticidade e estimulando o remapeamento cortical sináptico.

---

## 2. Métricas de Desempenho e Requisitos Clínicos

| Métrica | Especificação de Projeto | Justificativa Técnica / Clínica |
| :--- | :---: | :--- |
| **Latência Média de Resposta** | `< 380 ms` | Do limiar de intenção neural ao avanço inicial do torque motriz, garantindo acoplamento perceptual ao paciente. |
| **Precisão Angular no Membro** | `± 0,45°` | Garantida pelo microstepping 1/16 do motor de passo acoplado a redutor epicicloidal. |
| **Velocidade Angular Segura** | `25°/s` | Limite fisioterapêutico para preservação articular e prevenção de espasticidade. |
| **Torque Máximo Operacional** | `4,8 N·m` | Torque dinâmico na junta do cotovelo para sustentação ativa e passiva do antebraço. |

---

## 3. Planejamento Preliminar de Hardware e Software
- **Hardware de Processamento:** Microcontrolador ESP32 WROOM-32D Dual-Core (FreeRTOS).
- **Interface Neural:** Front-end de biopotencial para eletrodos secos nas derivações C3/Cz/C4 (sistema 10-20).
- **Atuação Mecânica:** Motor de passo NEMA 23 com redutor planetário e driver Trinamic TMC2208 StealthChop2.
- **Protocolo de Comunicação:** Envio de telemetria médica via REST/HTTPS sobre Wi-Fi para os servidores do HAOC.

---

## 4. Marcos Técnicos da 1ª Fase
1. Levantamento presencial com a equipe de fisioterapia e neurologia do Hospital Alemão Oswaldo Cruz.
2. Definição do escopo de graus de liberdade (flexão e extensão do cotovelo: 0° a 110°).
3. Elaboração dos requisitos de parada de emergência e segurança intrínseca do paciente.
