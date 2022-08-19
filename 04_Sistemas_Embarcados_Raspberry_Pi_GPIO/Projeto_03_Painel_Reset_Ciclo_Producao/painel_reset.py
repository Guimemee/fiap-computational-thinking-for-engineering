# Projeto RPi 3: Contador de Peças com Botão de Reset de Caixa pelo Operador
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

PIN_S1 = 17 # Sensor de entrada
PIN_S2 = 27 # Sensor de saída/queda
PIN_B1 = 23 # Botão de Reset no painel do operador
PIN_M1 = 24 # Motor da esteira
PIN_L1 = 22 # Lâmpada de alerta

GPIO.setmode(GPIO.BCM)
GPIO.setup([PIN_S1, PIN_S2, PIN_B1], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup([PIN_M1, PIN_L1], GPIO.OUT)

CAPACIDADE_MAXIMA = 20
contador_pecas = 0

def aguardar_borda(pino):
    while GPIO.input(pino) == 1:
        time.sleep(0.02)

print("Sistema de Contagem e Reset de Caixa Iniciado.")
try:
    while True:
        if contador_pecas < CAPACIDADE_MAXIMA:
            GPIO.output(PIN_L1, 0)
            print(f"Aguardando peça no sensor S1... ({contador_pecas}/{CAPACIDADE_MAXIMA})")
            aguardar_borda(PIN_S1)
            
            GPIO.output(PIN_M1, 1)
            aguardar_borda(PIN_S2)
            contador_pecas += 1
            print(f"Peça armazenada! Total: {contador_pecas}")
            
            if contador_pecas >= CAPACIDADE_MAXIMA:
                GPIO.output(PIN_M1, 0)
                GPIO.output(PIN_L1, 1)
                print(">> CAIXA CHEIA! Pressione o botão B1 no painel após realizar a troca.")
        else:
            aguardar_borda(PIN_B1)
            contador_pecas = 0
            GPIO.output(PIN_L1, 0)
            print(">> Botão B1 pressionado! Caixa substituída. Contador zerado. Ciclo reiniciado.\n")

except KeyboardInterrupt:
    GPIO.cleanup()
