import requests
import simplejson as json
from io import BytesIO
from PIL import Image

params = {"#q": 'pizza'}
r = requests.get("http://www.google.com", params=params)
print("Status:", r.status_code, ":", r.url)

f = open("./page.html", "w+")
f.write(r.text)

r = requests.get("https://images8.alphacoders.com/100/thumb-1920-1003220.png")
print("Status:", r.status_code, ":", r.url)

image = Image.open(BytesIO(r.content))
print(image.size, image.format, image.mode)
path = "./AvengersImg." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Can't save image")

# POST
my_data = {"name": "Natasha Romanov", "email": "nat_r@shield.int"}
r = requests.post("https://www.w3schools.com/php/welcome.php", data=my_data)

f = open('myfile.html', 'w+')
f.write(r.text)

payload = {"longUrl": "http://example.com"}
url = "https://www.googleapis.com/urlshortener/v1/url"
headers = {"Content-Type": "application/json"}
r = requests.post(url, json=payload, headers=headers)
print("Server headers:", r.headers)
print(json.loads(r.text)['error']['code'], ":", json.loads(r.text)['error']['message'])
