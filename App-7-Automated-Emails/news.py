import requests

# 160194a078264e7d82c5d9e6483039e6


class NewsFeed:
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "160194a078264e7d82c5d9e6483039e6"

    def __init__(self, interest, language="en"):
        self.interest = interest
        self.language = language


    def get(self):
        url = f"{self.base_url}qInTitle={self.interest}&" \
              f"from=2021-06-05&to=2021-06-06&language={self.language}" \
              f"&apiKey={self.api_key}"

        response = requests.get(url)
        content = response.json()
        print(content)
        articles = content['articles']

        email_body = ""
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body
