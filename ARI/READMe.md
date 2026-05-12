# Arquitetura IoT: Integração de Sistemas

Este documento detalha os fundamentos da arquitetura IoT, focando na coleta de dados com hardware e no processamento/comunicação via software.

---

## 1. O Hardware: Arduino
O Arduino atua na **Camada de Percepção**. Ele é responsável por interagir diretamente com o mundo físico através de sensores e atuadores.

- **Microcontrolador:** Geralmente ATmega328P (Arduino Uno).
- **Entradas/Saídas:** 
    - *Digitais:* Estados ON/OFF (0V ou 5V).
    - *Analógicas:* Leitura de valores variáveis (0 a 1023).
- **Função na Arquitetura:** Coleta de sinais analógicos/digitais e pré-processamento básico.

---

## 2. Linguagem de Programação: C++ (Firmware)
O Arduino é programado em uma variação de **C++**. É uma linguagem de baixo nível que permite controle total sobre o hardware.

### Estrutura do Código:
```cpp
// Definições de pinos
const int sensorPin = A0;

void setup() {
  Serial.begin(9600); // Inicia comunicação serial
  pinMode(sensorPin, INPUT);
}

void loop() {
  int valor = analogRead(sensorPin); // Lendo dados do sensor
  Serial.println(valor);           // Enviando para o computador/gateway
  delay(1000);                     // Intervalo de amostragem
}
```

---

## 3. Linguagem de Programação: Python (Backend/Gateway)
Enquanto o C++ roda no dispositivo, o **Python** costuma rodar em um Gateway (como um Raspberry Pi ou PC) ou no Servidor.

### Por que Python no IoT?
- **Bibliotecas:** `pyserial` para ler o Arduino, `paho-mqtt` para enviar dados para a nuvem.
- **Processamento:** Ideal para análise de dados e Inteligência Artificial.
- **Integração:** Facilidade para conectar com bancos de dados e APIs web.

### Exemplo de Script Python (Leitura Serial):
```python
import serial
import time

# Configuração da porta (ajustar conforme o SO)
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

def read_data():
    data = arduino.readline().decode('utf-8').strip()
    return data

while True:
    value = read_data()
    if value:
        print(f"Dados recebidos do Arduino: {value}")
    time.sleep(1)
```

---

## 4. Fluxo de Dados na Arquitetura
1. **Sensor** -> Detecta grandeza física.
2. **Arduino (C++)** -> Processa o sinal e envia via Serial/Wi-Fi.
3. **Gateway (Python)** -> Recebe os dados, trata e armazena ou envia para o Dashboard.
4. **Cloud/User Interface** -> Exibição para o usuário final.
