import requests

def get_top_headlines() -> requests.Response:
    response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json").json()[:10]
    return response

def get_headline_by_id(headline_id):
    headline = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{headline_id}.json")
    return headline.json()

def main():
    top_ten_ids = get_top_headlines()

    for index, headline_id in enumerate(top_ten_ids):
        headline = get_headline_by_id(headline_id)
        print(f"Headline {index + 1}.")
        print(f"Title: {headline['title']}")
        print(f"URL: {headline.get('url', 'No URL available')}")
        print("-" * 40)

if __name__ == "__main__":
    main()