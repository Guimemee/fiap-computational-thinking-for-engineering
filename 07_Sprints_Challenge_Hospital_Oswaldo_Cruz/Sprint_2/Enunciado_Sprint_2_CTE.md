# Sprint 2 — Arquitetura de Sistema e Diagrama Funcional em Malha Fechada
### Hospital Alemão Oswaldo Cruz • Challenge de Inovação em Saúde
**Projeto:** Exoesqueleto Ativo de Membro Superior com Interface Cérebro-Máquina (BMI/BCI)  
**Disciplina:** Computational Thinking for Engineering (CTE)  
**Curso:** Bacharelado em Engenharia da Computação • FIAP (Turma 1ECR)  
**Aluno:** Guilherme Macario da Silva — RM: 84053  
**Status:** CONCLUÍDO E VALIDADO ✅

---

## 1. Diagrama de Arquitetura do Sistema (*Closed-Loop*)

A arquitetura opera em malha fechada (*closed-loop*), dividida em quatro camadas funcionais interconectadas:

```mermaid
graph TD
    subgraph 1. Camada Neural (BCI)
        E[Eletrodos Córtex Motor C3/Cz/C4] --> F[Filtro Notch 60Hz + Bandpass 8-30Hz]
        F --> EXT[Extração de Ondas Mu e Beta]
        EXT --> S1[Saída: UART / BLE Intenção]
    end

    subgraph 2. Unidade Central (ESP32)
        S1 --> FSM[FSM de Controle de Estado e Segurança]
        FSM --> STEP[Geração de Pulsos STEP / DIR]
        ENC[Encoders AS5600 + Fim-de-Curso] --> FSM
    end

    subgraph 3. Potência Mecânica
        STEP --> DRV[Driver Silencioso TMC2208]
        DRV --> MOT[Motor de Passo NEMA 23]
        MOT --> RED[Redução Epicicloidal 1:10]
        RED --> ORT[Órtese / Junta Articular (4.8 N·m)]
    end

    subgraph 4. Telemetria Médica
        FSM --> GTW[Gateway Wi-Fi HTTPS / TLS 1.3]
        GTW --> JSON[Formato HL7 / FHIR JSON]
        JSON --> DASH[Dashboard Fisioterapeuta HAOC]
        DASH --> PRONT[Prontuário Oswaldo Cruz]
    end
```

---

## 2. Detalhamento das Camadas Funcionais

### 1. Camada Neural (BCI)
- Posicionamento de eletrodos em posições C3, Cz e C4 conforme sistema internacional 10-20.
- Filtro analógico e digital Notch de 60 Hz para eliminação de ruídos da rede elétrica, somado a filtro passa-faixa (*bandpass*) entre 8 Hz e 30 Hz.
- Extração de potência espectral das bandas Mu (8–12 Hz) e Beta (13–30 Hz) associadas ao planejamento motor.

### 2. Unidade Central (ESP32)
- Máquina de Estados Finitos (FSM) com transições determinísticas entre: `IDLE`, `LEITURA_NEURAL`, `MOVIMENTO_ATIVO`, `PAUSA_TERAPÊUTICA` e `EMERGÊNCIA`.
- Geração precisa de micropassos via interrupção temporizada por hardware.
- Realimentação contínua de ângulo por encoder absoluto magnético AS5600 (I2C) e microswitches nas posições angulares limites (0° e 110°).

### 3. Potência Mecânica
- Driver Trinamic TMC2208 operando com tecnologia *StealthChop2*, reduzindo o ruído acústico a patamares imperceptíveis para não dispersar o paciente.
- Motor de passo NEMA 23 com torque estático de 18 kgf·cm acoplado a caixa redutora planetária 1:10, fornecendo 4,8 N·m de torque contínuo seguro.

### 4. Telemetria Médica e Segurança
- Despacho assíncrono de relatórios clínicos em formato JSON via mTLS diretamente aos servidores em nuvem do Hospital Alemão Oswaldo Cruz.
- **Segurança Intrínseca:** Firmware monitora interruptores mecânicos e limite de corrente em tempo real. Qualquer desacoplamento do eletrodo ou desvio de trajetória corta imediatamente a alimentação dos enrolamentos (*E-Stop* por hardware).
