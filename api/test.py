import requests

files = {'file': open('boat.jpg', 'rb')}
res = requests.post("http://localhost:5000/predict", files=files)
print(res.json())