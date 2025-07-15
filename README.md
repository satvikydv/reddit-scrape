
# Reddit User Persona Generator (LLM-powered)

This project scrapes Reddit posts and comments from a user's public profile and generates a detailed **User Persona** using **Google's Gemini LLM**. The persona includes inferred traits like motivations, personality, frustrations, and more — with citations from the user’s activity.

---

##  Features

- Scrapes Reddit user's **posts** and **comments**
- Uses **Gemini (Google's LLM)** to generate a UX-style persona
- Persona output includes:
  - Name, Age, Occupation, Status, Location
  - Archetype & Personality
  - Motivations, Behavior, Frustrations, Goals
  - **Citations** from Reddit posts/comments
- Output saved as a clean `.txt` file

---

## 📦 Requirements

- Python 3.8+
- A Reddit account (for API credentials)
- Gemini API key (via Google AI Studio)

---

## 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/reddit-persona-generator.git
   cd reddit-persona-generator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the root folder and add:

   ```env
   # Reddit API (PRAW)
   REDDIT_CLIENT_ID=your_reddit_client_id
   REDDIT_SECRET=your_reddit_secret
   REDDIT_USERNAME=your_reddit_username
   REDDIT_PASSWORD=your_reddit_password

   # Gemini LLM
   GEMINI_API_KEY=your_gemini_api_key
   ```

---

## 📝 Setup Reddit API (PRAW)

1. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Click **“Create App”**
3. Choose `script`, give a name, and set `http://localhost:8080` as redirect URI
4. Copy the `client_id` and `secret` and add them to `.env`

---

## 🧠 Get Gemini API Key

1. Visit: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. Click **"Create API key"**
3. Paste it in your `.env` under `GEMINI_API_KEY`

---

## ✅ How to Use

### 1. Scrape a Reddit user's data:

```bash
python reddit_scraper.py
```

Update the script or run in Python REPL:

```python
from reddit_scraper import scrape_redditor
scrape_redditor("Hungry-Move-6603", max_items=50)
```

This will create a file like: `Hungry-Move-6603_reddit_data.json`

---

### 2. Generate a user persona from the scraped data:

```bash
python generate_persona_gemini.py
```

Make sure the file has:
```python
if __name__ == "__main__":
    generate_persona_from_data("Hungry-Move-6603", "Hungry-Move-6603_reddit_data.json")
```

This generates a file like:  
📄 `user_persona_Hungry-Move-6603.txt`

---

## 🤖 Requirements

```txt
praw
tqdm
python-dotenv
google-generativeai
```

---

## 📌 Notes

- You can adjust `max_items=50` to scrape more or fewer posts/comments.
- Gemini input is limited to ~15,000 characters, so longer Reddit profiles are truncated.

---

## 📬 License
MIT — Free to use, modify, and share.
