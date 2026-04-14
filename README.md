# binance-trading-bot

## 📌 Overview

This project is a **Python-based CLI trading bot** that allows users to place **MARKET** and **LIMIT** orders on the Binance Futures Testnet.

It is designed with a **clean modular architecture**, proper **logging**, and robust **error handling**, making it suitable for production-style backend development.

---

## ⚙️ Features

* ✅ Place **MARKET orders** (BUY / SELL)
* ✅ Place **LIMIT orders**
* ✅ Supports Binance Futures Testnet (safe environment)
* ✅ CLI-based input using `click`
* ✅ Input validation (symbol, type, quantity, etc.)
* ✅ Logging of API requests, responses, and errors
* ✅ Order status tracking (NEW → FILLED handling)

---

## 🏗️ Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py        # Binance client wrapper
│   ├── orders.py        # Order placement logic
│   ├── validators.py    # Input validation
│   ├── logging_config.py
│
├── logs/
│   └── trading.log      # Logs for API calls and errors
│
├── cli.py               # CLI entry point
├── requirements.txt
├── README.md
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone the repository

```
git clone <your-repo-link>
cd trading_bot
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Create `.env` file

Create a `.env` file in the root directory:

```
API_KEY=your_binance_api_key
API_SECRET=your_binance_secret_key
```

> ⚠️ Note: Use **Binance Futures Testnet API keys only**

---

## ▶️ Usage

### 🔹 MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### 🔹 LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 80000
```

---

## 📊 Sample Output

### ✅ MARKET Order (Executed)

```
Order Response:
Status: NEW

Updated Order Status:
Status: FILLED
Executed Qty: 0.0010
Avg Price: 74351.50
```

---

### ⚠️ LIMIT Order (Not Executed Yet)

```
Status: NEW
Executed Qty: 0.0000

Updated Order Status:
Status: NEW
Executed Qty: 0.0000
```

> ℹ️ LIMIT orders execute only when market price matches the specified price.

---

## 🧠 Assumptions

* The bot uses **Binance Futures Testnet** (no real money involved)
* User must have **test USDT balance**
* MARKET orders execute immediately
* LIMIT orders depend on price matching

---

## 📁 Logs

All logs are stored in:

```
logs/trading.log
```

Logs include:

* API request details
* Order responses
* Errors and exceptions

---

## 📦 Requirements

```
python-binance
python-dotenv
click
---

## 🚀 Future Improvements (Optional)

* Stop-Limit order support
* Better CLI UX (interactive prompts)
* Web-based UI dashboard
* Strategy-based trading automation

---

## 👨‍💻 Author

Developed as part of Python Developer Application Task (Trading Bot)

---
