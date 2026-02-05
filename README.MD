
# 🤖 Bot Binance – Trading Automatizado com Dashboard

Bot de trading **Spot na Binance**, desenvolvido em **Python**, com:
- Estratégia técnica automatizada
- Controle de risco (TP / SL)
- Recovery automático de posição
- Dashboard em **Streamlit**
- Controle do bot via Frontend
- Logs e histórico de operações

> ⚠️ **Aviso**: Este projeto é educacional. Trading envolve risco. Use com valores pequenos.

---

## 📌 Funcionalidades

### ✅ Backend (Bot)
- Conexão com API da Binance (Spot)
- Estratégia baseada em indicadores técnicos
- Compra e venda automática
- Take Profit e Stop Loss
- Recovery automático do preço de entrada
- Proteção contra mínimo da Binance
- Logs de status em tempo real
- Histórico estruturado de trades (CSV)

### ✅ Frontend (Dashboard)
- Painel de controle em Streamlit
- Exibição de:
  - Lucro / Prejuízo (PnL)
  - Total comprado e vendido
  - Número de trades
  - Histórico completo
  - Status atual do bot (console)
- Botões para:
  - Iniciar bot
  - Pausar bot

---

## 📁 Estrutura do Projeto

```
Bot-Binance/
├── bot/
│ ├── main.py # Loop principal do bot
│ ├── trader.py # Ordens e dados da Binance
│ ├── strategy.py # Regras de compra
│ ├── indicators.py # Indicadores técnicos
│ ├── trade_history.py # Registro estruturado de trades
│ ├── logger.py # Logs e status do bot
│ ├── trade_history.csv # Histórico de operações
│ ├── bot_status.log # Status em tempo real
│ ├── bot_control.json # Controle via dashboard
│
├── dashboard/
│ └── app.py # Frontend Streamlit
│
├── .env # Variáveis de ambiente (NÃO versionar)
├── .gitignore
├── requirements.txt
└── README.md
```



---

## 🔐 Configuração da API Binance

1. Acesse:
 Binance → Perfil → API Management 

 
2. Crie uma nova API Key

3. Permissões:
- ✅ Enable Reading
- ✅ Enable Spot Trading
- ❌ Withdrawals (NÃO habilitar)

4. (Opcional) Restrinja por IP

---

## ⚙️ Variáveis de Ambiente (`.env`)

Crie um arquivo `.env` na raiz:

```env
BINANCE_API_KEY=SUACHAVEAQUI
BINANCE_API_SECRET=SUASECRETAQUI
```
⚠️ Nunca suba esse arquivo para o GitHub.

---

📦 Instalação
1️⃣ Clone o repositório
```
git clone https://github.com/seu-usuario/bot-binance.git
```
```
cd bot-binance
```
2️⃣ Crie um ambiente virtual
```
python -m venv .venv
```
```
source .venv/bin/activate  # Linux/Mac
```
```
.venv\Scripts\activate     # Windows
```
```
python -m venv .venv
```
```
source .venv/bin/activate  # Linux/Mac
```
```
.venv\Scripts\activate     # Windows
```
3️⃣ Instale dependências
pip install -r requirements.txt

---
▶️ Executando o Bot

Na raiz do projeto:

python bot/main.py


O bot:

lê o arquivo bot_control.json

só opera se "run": true
---

🖥️ Executando o Dashboard
streamlit run dashboard/app.py


Acesse:

http://localhost:8501

---

🎛️ Controle do Bot pelo Frontend

O dashboard não executa código diretamente.
Ele escreve comandos em:

bot/bot_control.json


Exemplo:

{ "run": true }


O bot lê esse arquivo continuamente e:

▶️ opera quando true

⏸️ pausa quando false

---
📊 Cálculo de Lucro / Prejuízo (PnL)

O PnL exibido no dashboard é realizado, baseado em trades fechados:

PnL = Total Vendido − Total Comprado


Apenas operações BUY + SELL contam

Trades abertos não entram no cálculo

Taxas da Binance não são descontadas (PnL bruto)

---
🧠 Estratégia Atual

Timeframe configurável

Compra baseada em indicadores técnicos

Apenas uma posição por vez

Sem DCA

Sem alavancagem

Spot only

---
🔒 Proteções Implementadas

❌ Compra sem USDT

❌ Compra com posição aberta

❌ Venda abaixo do mínimo da Binance

❌ Execução quando bot está pausado

✅ Recovery automático após restart

✅ Uso do saldo real da carteira

---
📝 Logs e Monitoramento

bot_status.log
→ Status em tempo real (console do bot)

trade_history.csv
→ Histórico estruturado para o dashboard

---

🚀 Próximos Upgrades Possíveis

Trailing Stop

DCA automático

Preço médio real

Gráfico de equity curve

Gráfico BTC + trades

Forçar venda pelo dashboard

Multi-par

Deploy em cloud (VPS / Docker)
---
⚠️ Aviso Legal

Este projeto não é recomendação financeira.
Use apenas valores que você pode perder.
O autor não se responsabiliza por prejuízos.
---
👨‍💻 Autor

Projeto desenvolvido por **Elisangela Miranda dos Anjos** para desenvolvido como projeto educacional para aprendizado de:

Python

APIs

Trading automatizado

Arquitetura backend + frontend