# Binance Futures Testnet Trading Bot (Python)

## Overview
This project is a simplified **Python-based trading bot** that places orders on **Binance Futures Testnet (USDT-M)** using the `python-binance` library.

The application is built with a **clean, modular structure**, provides a **CLI interface**, includes **robust logging**, and handles **common real-world API errors** such as authentication issues, timestamp drift, and minimum notional constraints.

This project was developed as part of a hiring assignment.

---

## Features
- Place **MARKET** and **LIMIT** orders on Binance Futures Testnet
- Supports both **BUY** and **SELL** sides
- Command-line interface using `argparse`
- Input validation (symbol, side, order type, quantity, price)
- Proper separation of concerns (client, orders, validation, CLI)
- Detailed logging of API requests, responses, and errors
- Robust error handling for:
  - Invalid API keys
  - Timestamp drift (`recvWindow`)
  - Binance Futures minimum notional rules

---

## Project Structure

trading_bot/
│
├── bot/
│ ├── init.py
│ ├── client.py # Binance Futures client wrapper
│ ├── orders.py # Order placement logic
│ ├── validators.py # CLI input validation
│ ├── logging_config.py # Logging configuration
│
├── cli.py # CLI entry point
├── logs/
│ └── orders.log # API request/response logs
├── requirements.txt
├── README.md


---

## Prerequisites
- Python **3.9+**
- Windows / PowerShell
- Binance Futures **Testnet account**

---

## Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone <your-github-repo-url>
cd trading_bot
2️⃣ Create and activate virtual environment (Windows)
python -m venv venv
.\venv\Scripts\Activate.ps1
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Create Binance Futures Testnet API Keys

Register at: https://testnet.binancefuture.com

Generate Futures Testnet API Key & Secret

Ensure:

Futures permission enabled

IP restriction disabled

5️⃣ Set environment variables (PowerShell)
setx BINANCE_API_KEY "YOUR_API_KEY"
setx BINANCE_API_SECRET "YOUR_API_SECRET"

⚠️ Restart PowerShell after setting variables.

Running the Application
▶ Place a MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
▶ Place a LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 75000
Output Example
Order Summary
------------------------------
Order ID: 12331327844
Status: FILLED
Executed Qty: 0.002
Avg Price: 68292.50
SUCCESS
Logs

All API requests, responses, and errors are logged to:

logs/orders.log
The log file includes:

Early setup errors (authentication, timestamp drift)

Binance Futures validation errors (minimum notional)

Successful MARKET and LIMIT order executions

This demonstrates robust logging and error handling in real-world API integration.