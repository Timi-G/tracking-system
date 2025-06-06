import random
import requests
# rand_list =

# list_comprehension_below_10 =

# list_comprehension_below_10 =

response=requests.get('http://localhost:8000/api/books/')
if response.status_code ==200:
    data=response.json()
    print(type(data),data[0]['author'])

send=  {
        "first_name": "Bud",
        "last_name": "Veral",
        "biography": "Lopper"
    }

sent=requests.post('http://localhost:8000/api/authors/',json=send)
print(sent.text)
