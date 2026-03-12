import requests

# site: https://httpbin.org/ is used for practicing requests library, with get, post and other http methods

base_url = 'https://httpbin.org/'

# GET request with parameters
# args = {'page':2, 'count':25}
# r = requests.get('https://httpbin.org/get',params=args)

# print(r.text)

# # POST request with form (body)
# body = {'username': 'sumit', 'age':22}
# post_response = requests.post(f'{base_url}/post',data=body)

# # gives full response with url, headers, args, form and other fields
# print(post_response.text) 
# json_response_as_dict = post_response.json()
# print(json_response_as_dict)


# httpbin allows us to perform basic auth as well (not just form based auth)


# Auth basic 
# username='guest'
# password='1234'

# auth = requests.get(f'{base_url}/basic-auth/{username}/{password}',auth=('asd;f',password))
# print(auth.text)
# print(auth.status_code)


# dealing with delayed responses (timeout)

delayed_res = requests.get(f'{base_url}/delay/1',timeout=5)
print(delayed_res.text)