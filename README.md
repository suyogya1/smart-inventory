# 📦 SmartInventory

SmartInventory is an intelligent inventory management system built with FastAPI, Streamlit, and AI. It tracks stock levels, sends automated alerts, and provides AI-powered reorder suggestions using Groq's LLM.

---

## 🚀 Features

- ✅ Add, update, and list inventory items
- ⚠️ Low stock detection with real-time warnings
- 🔁 Email alerts using n8n (triggered via webhook)
- 🤖 AI-powered reorder suggestions using Groq's LLM
- 📊 Clean, interactive Streamlit dashboard
- 🧠 FastMCP routing engine for modular decision-making

---

## 🧱 Tech Stack

| Layer        | Technology                          |
|--------------|--------------------------------------|
| Frontend     | Streamlit (Python)                  |
| Backend      | FastAPI (Python), Uvicorn           |
| AI           | Groq (Llama3-8b-8192)               |
| Automation   | n8n (local via webhook)             |
| Routing Core | FastMCP (custom task router)        |
| Data Store   | In-memory dictionary (for now)      |

---

## 📸 Screenshots

> _(Add screenshots of the dashboard, low stock alert, and AI response section here if you'd like)_

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/smartinventory.git
cd smartinventory

# Install dependencies
pip install -r requirements.txt

# Set your Groq API Key
echo "GROQ_API_KEY=your_groq_api_key" > .env

# Start the backend
uvicorn backend.main:app --reload

# In another terminal, start the frontend
streamlit run frontend/app.py
