import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_reorder_suggestions(inventory_dict):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are an inventory assistant.

Here is the current inventory:
{inventory_dict}

List 3 items that should be reordered soon due to low stock, and briefly explain why for each.
"""

    payload = {
        "model": "llama3-8b-8192",  
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)
    
    # ✅ Raise helpful error if something's wrong
    if response.status_code != 200:
        raise Exception(f"Groq API error {response.status_code}: {response.text}")
    
    return response.json()['choices'][0]['message']['content']
