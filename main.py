import requests
from send_email import send_email

api_key = "96db5ae4e191484d98de360414df940c"
url = "https://newsapi.org/v2/everything?q=tesla&"\
        "from=2023-03-14&sortBy=publishedAt&apiKey="\
        "96db5ae4e191484d98de360414df940c"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)
