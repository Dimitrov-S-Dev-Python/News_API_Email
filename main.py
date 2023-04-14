import requests

api_key = "96db5ae4e191484d98de360414df940c"
url = "https://newsapi.org/v2/everything?q=tesla&"\
        "from=2023-03-14&sortBy=publishedAt&apiKey="\
        "96db5ae4e191484d98de360414df940c"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["titles"])
