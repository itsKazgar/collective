#!/usr/bin/env python3
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.expanduser("~/BR0THA_bot/.env"))

def test_groq():
    try:
        from groq import Groq
        client = Groq(api_key=os.environ["GROQ_API_KEY"])
        r = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "Say OK"}],
            max_tokens=5,
        )
        return "✅ " + r.choices[0].message.content.strip()
    except KeyError:
        return "❌ GROQ_API_KEY not found in .env"
    except Exception as e:
        return f"❌ {e}"

def test_gemini():
    try:
        from google import genai
        client = genai.Client(api_key=os.environ["GEMINI_DIRECT_KEY"])
        r = client.models.generate_content(
            model="gemini-2.0-flash",
            contents="Say OK",
        )
        return "✅ " + r.text.strip()
    except KeyError:
        return "❌ GEMINI_DIRECT_KEY not found in .env"
    except Exception as e:
        return f"❌ {e}"

def test_cerebras():
    try:
        from cerebras.cloud.sdk import Cerebras
        client = Cerebras(api_key=os.environ["CEREBRAS_API_KEY"])
        r = client.chat.completions.create(
            model="llama3.1-8b",
            messages=[{"role": "user", "content": "Say OK"}],
            max_tokens=5,
        )
        return "✅ " + r.choices[0].message.content.strip()
    except KeyError:
        return "❌ CEREBRAS_API_KEY not found in .env"
    except Exception as e:
        return f"❌ {e}"

def test_kimi():
    try:
        from openai import OpenAI
        client = OpenAI(
            api_key=os.environ["OPENROUTER_API_KEY"],
            base_url="https://openrouter.ai/api/v1",
        )
        r = client.chat.completions.create(
            model="moonshotai/kimi-k2",
            messages=[{"role": "user", "content": "Say OK"}],
            max_tokens=5,
        )
        return "✅ " + r.choices[0].message.content.strip()
    except KeyError:
        return "❌ OPENROUTER_API_KEY not found in .env"
    except Exception as e:
        return f"❌ {e}"

def test_deepseek():
    try:
        from openai import OpenAI
        client = OpenAI(
            api_key=os.environ["OPENROUTER_API_KEY"],
            base_url="https://openrouter.ai/api/v1",
        )
        r = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[{"role": "user", "content": "Say OK"}],
            max_tokens=5,
        )
        return "✅ " + r.choices[0].message.content.strip()
    except KeyError:
        return "❌ OPENROUTER_API_KEY not found in .env"
    except Exception as e:
        return f"❌ {e}"

def test_openrouter():
    try:
        from openai import OpenAI
        client = OpenAI(
            api_key=os.environ["OPENROUTER_API_KEY"],
            base_url="https://openrouter.ai/api/v1",
        )
        r = client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct:free",
            messages=[{"role": "user", "content": "Say OK"}],
            max_tokens=5,
        )
        return "✅ " + r.choices[0].message.content.strip()
    except KeyError:
        return "❌ OPENROUTER_API_KEY not found in .env"
    except Exception as e:
        return f"❌ {e}"

tests = {
    "Groq":       test_groq,
    "Gemini":     test_gemini,
    "Cerebras":   test_cerebras,
    "Kimi":       test_kimi,
    "DeepSeek":   test_deepseek,
    "OpenRouter": test_openrouter,
}

print("\n🔍 Testing all providers...\n")
print(f"{'Provider':<12} Result")
print("-" * 40)
for name, fn in tests.items():
    result = fn()
    print(f"{name:<12} {result}")
print("\nDone!\n")
