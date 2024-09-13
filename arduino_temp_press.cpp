// Inclusão das bibliotecas
#include <OneWire.h>
#include <DallasTemperature.h>

// Configuração do sensor de temperatura DS18B20
const int PINO_ONEWIRE = 12; // Define o pino do sensor de temperatura
OneWire oneWire(PINO_ONEWIRE); // Cria um objeto OneWire
DallasTemperature sensor(&oneWire); // Informa a referência da biblioteca DallasTemperature para a biblioteca OneWire
DeviceAddress endereco_temp; // Cria um endereço temporário para a leitura do sensor

// Configuração do sensor de pressão XGZP101DB1R
const int PINO_PRESSAO = A0; // Pino analógico conectado ao VO+
float ant = 0; // Variável para armazenar a pressão anterior

void setup() {
  // Inicia a comunicação serial
  Serial.begin(9600); //Inicia a comunicação serial com uma taxa de transmissão de 9600 bps (bits por segundo), permitindo enviar e receber dados entre o Arduino e o computador
  Serial.println("Medindo Temperatura e Pressão"); // Mensagem inicial
  
  // Inicia o sensor de temperatura
  sensor.begin();
}

void loop() {
  // Leitura da temperatura
  sensor.requestTemperatures(); // Envia comando para realizar a conversão de temperatura
  float temperatura = 0.0;
  if (!sensor.getAddress(endereco_temp, 0)) { // Tenta obter o endereço no barramento do sensor de temperatura
    Serial.println("SENSOR DE TEMPERATURA NÃO CONECTADO"); // Sensor não conectado, imprime mensagem de erro
  } else {
    temperatura = sensor.getTempC(endereco_temp); // Busca temperatura para o dispositivo
  }
  
  // Leitura da pressão
  int leituraBruta = analogRead(PINO_PRESSAO); // Lê o valor analógico do sensor de pressão, o valor retornado será entre 0 e 1023, correspondente a uma tensão entre 0 e 5V
  float tensao = leituraBruta * (5.0 / 1023.0); // Converte o valor lido do ADC (Conversor Analógico-Digital) em uma tensão real (em volts)
  
  // Conversão da tensão para pressão
  float pressao = (tensao / 5.0) * 201.62; 
  
  // Envia os valores para o Serial Plotter
  Serial.print(temperatura, 1); // Imprime a temperatura com 1 casa decimal
  Serial.print("\n"); // Separador entre temperatura e pressão
  Serial.println(pressao); // Imprime a pressão

  // Atualiza a pressão anterior
  ant = pressao;

  // Aguarda 1 segundo antes de ler novamente
  delay(1000);
}
