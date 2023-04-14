import requests
from send_email import send_email

topic = "tesla"

api_key = "96db5ae4e191484d98de360414df940c"
url = "https://newsapi.org/v2/everything?"\
    f"q={topic}&" \
    "from=2023-03-14&" \
    "sortBy=publishedAt&" \
    "apiKey=96db5ae4e191484d98de360414df940c&" \
    "language=en"

# Make request
response = requests.get(url)

# Get a dictionary with data
content = response.json()

# Access the article titles and description
body = ""
for article in content["articles"][:5]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] +\
               "\n" + article["description"] +\
               "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)
