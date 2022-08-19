# Projeto RPi 2: Contador de Peças com Alerta de Caixa Lotada

> 2-) No sistema abaixo quando uma peça é colocada na posição dada pelo sensor S1 o motor M1 é ligado, levando a peça até o sensor S2 e caindo na caixa de saída. Sabe-se que a caixa suporta até 20 peças. Implemente um contador para que quando 20 peças caírem na caixa o motor M1 seja desligado e a lâmpada L1 ligada, alertando ao operador a necessidade de trocar a caixa. Elabore um programa que atenda o solicitado.
> 
> **Considerar:**
> - `S1` e `S2`: simular os sensores com Pushbuttons.
> - `L1`: simular a lâmpada com um LED.
> - `M1`: DC Motor acionado por GPIO.


<div align="center">
  <img src="../../assets/rpi_images/rpi_exercicio_2_Image12.jpg" alt="Diagrama da Esteira com Caixa e Lâmpada L1" width="520">
</div>

### Link do Código:
- 🔗 [`contador_pecas.py`](./contador_pecas.py)

### Resolução:
```python
# Projeto RPi 2: Contador de Peças Industriais com Alerta de Lotação
import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    class MockGPIO:
        BCM = OUT = IN = PUD_UP = 0
        def setmode(self, m): pass
        def setup(self, p, mode, pull_up_down=None): pass
        def output(self, p, val): pass
        def input(self, p): return 1
        def cleanup(self): pass
    GPIO = MockGPIO()

PIN_S1 = 17 # Sensor de entrada da peça
PIN_S2 = 27 # Sensor de queda na caixa
PIN_M1 = 24 # Motor DC da esteira
PIN_L1 = 22 # Lâmpada de alerta (LED)

GPIO.setmode(GPIO.BCM)
GPIO.setup([PIN_S1, PIN_S2], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup([PIN_M1, PIN_L1], GPIO.OUT)

CAPACIDADE_MAXIMA = 20
contador_pecas = 0

def aguardar_borda(pino):
    while GPIO.input(pino) == 1:
        time.sleep(0.02)

print("Sistema de Contagem de Peças Iniciado.")
try:
    while True:
        if contador_pecas < CAPACIDADE_MAXIMA:
            GPIO.output(PIN_L1, 0)
            print(f"Aguardando peça no sensor S1... (Contagem atual: {contador_pecas}/{CAPACIDADE_MAXIMA})")
            aguardar_borda(PIN_S1)
            
            print("Peça inserida! Ligando motor M1...")
            GPIO.output(PIN_M1, 1)
            
            aguardar_borda(PIN_S2)
            contador_pecas += 1
            print(f"Peça caiu na caixa! Total acumulado: {contador_pecas}")
            
            if contador_pecas >= CAPACIDADE_MAXIMA:
                GPIO.output(PIN_M1, 0)
                GPIO.output(PIN_L1, 1)
                print(">> ALERTA: Caixa lotada com 20 peças! Motor desligado. Troque a caixa.")
        else:
            time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
```
