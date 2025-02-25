import requests

endpoint = "https://najottalim.uz/"

get_response = requests.get(endpoint) #API => (Aplication Programming Interface) -> Method the get() is https request method
print(get_response.json()) #this returns raw response #it is https request
# with open("response.html", "w", encoding="utf-8") as file:
#     file.write(get_response.json())



# HTTPS Request -> return HTML
# REST API Request -> returns JSON=> JavaScript Object Nototion ~ Python dic
