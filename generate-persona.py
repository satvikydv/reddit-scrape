import json
import os
from dotenv import load_dotenv
from tqdm import tqdm
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are a UX researcher. Your task is to generate a user persona based on Reddit posts and comments.
Analyze the user's Reddit activity and infer the following fields:
- Name (use Reddit username or a similar creative name)
- Age (guess based on context)
- Occupation
- Status (relationship, family, etc.)
- Location (if any clues)
- Archetype (e.g. The Creator, The Analyst)
- Personality (MBTI style if possible)
- Motivations (with supporting quote/URL)
- Behavior & Habits (with examples)
- Frustrations (with quotes/URLs)
- Goals & Needs (with examples)
Use Reddit content citations from the user's posts/comments when appropriate.
Format your output clearly like a UX persona document.
"""

def read_scraped_data(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def format_user_data(posts, comments, max_chars=15000):
    """
    Returns a chunk of user text (posts and comments) for Gemini.
    """
    data = ""
    for p in posts:
        data += f"\n[Post: {p['title']}]\n{p['selftext']}\n(Source: {p['url']})\n"
    for c in comments:
        data += f"\n[Comment]\n{c['body']}\n(Source: {c['url']})\n"
        if len(data) > max_chars:
            break
    return data[:max_chars]

def generate_persona_from_data(username, json_path):
    print(f"Generating persona for: {username}")
    user_data = read_scraped_data(json_path)
    text_chunk = format_user_data(user_data["posts"], user_data["comments"])

    model = genai.GenerativeModel('gemini-2.5-pro')

    response = model.generate_content([
        SYSTEM_PROMPT,
        text_chunk
    ])

    persona = response.text

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"user_persona_{username}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"Persona saved to {output_path}")


if __name__ == "__main__":
    generate_persona_from_data("Hungry-Move-6603", "output\Hungry-Move-6603_reddit_data.json")
