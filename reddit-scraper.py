# reddit_scraper.py

import praw
import os
import json
from tqdm import tqdm

from dotenv import load_dotenv
load_dotenv()


# Load Reddit credentials from environment variables (for security)
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
REDDIT_USER_AGENT = "user_persona_script"

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_SECRET,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
    user_agent=REDDIT_USER_AGENT
)

def scrape_redditor(username, max_items=100):
    redditor = reddit.redditor(username)

    scraped_data = {"username": username, "posts": [], "comments": []}

    # Scrape submissions
    print(f"Fetching posts from u/{username}...")
    try:
        for submission in tqdm(redditor.submissions.new(limit=max_items)):
            scraped_data["posts"].append({
                "title": submission.title,
                "selftext": submission.selftext,
                "subreddit": str(submission.subreddit),
                "score": submission.score,
                "url": f"https://www.reddit.com{submission.permalink}"
            })
    except Exception as e:
        print(f"Error fetching submissions: {e}")

    # Scrape comments
    print(f"Fetching comments from u/{username}...")
    try:
        for comment in tqdm(redditor.comments.new(limit=max_items)):
            scraped_data["comments"].append({
                "body": comment.body,
                "subreddit": str(comment.subreddit),
                "score": comment.score,
                "url": f"https://www.reddit.com{comment.permalink}"
            })
    except Exception as e:
        print(f"Error fetching comments: {e}")

    # Save to JSON
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"{username}_reddit_data.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(scraped_data, f, indent=2, ensure_ascii=False)

    print(f"\nSaved data to {filename}")
    return scraped_data

if __name__ == "__main__":
    # enter any Reddit username you want to scrape
    username = "Hungry-Move-6603"
    scrape_redditor(username)
