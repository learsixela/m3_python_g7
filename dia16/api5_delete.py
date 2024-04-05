import requests

url = "https://jsonplaceholder.typicode.com/posts/10"


response = requests.delete(url)

print(response.text)
print(response.status_code)#200