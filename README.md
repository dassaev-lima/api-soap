# Projeto SOAP IMC

Este projeto fornece um serviço SOAP para calcular o Índice de Massa Corporal (IMC) com base em peso e altura. O projeto é dividido em duas partes: um servidor SOAP em Python e um cliente em Node.js.

## Requisitos

- Python 3.x
- Node.js e npm (Node Package Manager)

## Configuração e Execução do Servidor

1. **Instalar Dependências**

   Certifique-se de que o `spyne` está instalado. Você pode instalar `spyne` usando o `pip`:

   ```bash
   pip install spyne

   pip install lxml

   ```

   Certifique-se de que o `soap` está instalado. Navegue até o diretório do cliente e instale a dependência `soap` usando o `npm`:

   ```bash
   npm install

   npm install soap
   ```

## Como Rodar o Projeto

1. **Navegue até o diretório do servidor:**

   ```bash
   cd python/

   python server.py
   ```

2. **Navegue até o diretório do cliente:**

   ```bash
   cd nodejs/src/

   node client.js
   ```
