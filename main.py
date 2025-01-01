import requests
from send_email import send_email 

api_key = "038e5f6ccdc14b74997caa208d508650" # taking from https://newsapi.org link
url = "https://newsapi.org/v2/everything?q=apple&from=2024-12-27&to=2024-12-27&sortBy=popularity&apiKey=038e5f6ccdc14b74997caa208d508650&language=en"

# url = "https://finance.yahoo.com"

request =requests.get(url)
# content=request.textcontent =request.json # for creating str
content =request.json() # for creating dictionary
# check dictionary for same
# print(content)

body = " "

for contents in content["articles"][0:21]:
    if contents["title"] and contents["description"] is not None:
        body ="Subject: Today's News"  \
        + "\n" + body + contents["title"] + "\n" \
        + contents["description"] + "\n" + contents["url"] + 2*"\n"

# print(body)
body =body.encode("UTF-8")
send_email(body)