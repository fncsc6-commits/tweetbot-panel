import requests
import os

GROQ_API_KEY = os.environ.get("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")

def generate_tweet():
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a gaming & esports breaking-news bot. "
                    "Write a tweet under 230 characters in English. "
                    "Topics: video games, esports teams, updates, events, celebrities. "
                    "No fake info, no speculation. Keep it hype but professional."
                )
            },
            { "role": "user", "content": "Generate one tweet." }
        ]
    }

    r = requests.post(url, json=data, headers=headers)
    tweet = r.json()["choices"][0]["message"]["content"]
    return tweet.strip()
