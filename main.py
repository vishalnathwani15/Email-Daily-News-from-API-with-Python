import requests

api_key = "038e5f6ccdc14b74997caa208d508650"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-11-28&sortBy=publishedAt&apiKey=038e5f6ccdc14b74997caa208d508650"

# url = "https://finance.yahoo.com"

request =requests.get(url)
# content=request.textcontent =request.json # for creating str
content =request.json() # for creating dictionary
for content in content["articles"]:
    print(content["title"])
    print(content["description"])