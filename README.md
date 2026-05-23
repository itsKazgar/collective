# BR0THA Bot
Solana AI trading dashboard with multi-model agent council.

## Stack
- Dashboard: brotha_dashboard.html (deploy to Netlify)
- API: brotha_api.py (deploy to Render/Railway)
- AI: Claude, GPT-4o, Grok, Gemini, Groq, OpenRouter

## Run locally
```bash
source venv/bin/activate
uvicorn brotha_api:app --host 0.0.0.0 --port 8000
```
