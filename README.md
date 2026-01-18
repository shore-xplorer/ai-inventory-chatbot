# AI Inventory Chatbot
An AI-powered simulation for grocery store inventory management using ChatGPT. Ask questions like "What's low on stock?" or "Forecast demand for milk next week" — it handles restock alerts, promotions for overstock, and basic predictions.

## Features
- Natural language queries for inventory status
- Simulated database (in-memory or simple JSON/CSV)
- Restock alerts & overstock promotions
- Demand forecasting via AI prompts

## Setup
1. Clone the repo: `git clone https://github.com/shore-xplorer/ai-inventory-chatbot.git`
2. Install deps: `pip install -r requirements.txt` (include openai, maybe flask/streamlit for UI)
3. Add your OpenAI API key to `.env`: `OPENAI_API_KEY=sk-...`
4. Run: `python app.py`

## Known Issues & Improvements
- Crashes on long/complex prompts → Working on better error handling & token limiting.
- Next: Add real DB (SQLite), web UI, or deploy as demo.

Contributions welcome! Star if useful.