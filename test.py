from algo import return_summary
import requests


# summary=return_summary("")
# print(summary)

data = {"text": "Your text data goes here"}
response=requests.post("http://127.0.0.1:5000/dummy",json=data)

print(response)