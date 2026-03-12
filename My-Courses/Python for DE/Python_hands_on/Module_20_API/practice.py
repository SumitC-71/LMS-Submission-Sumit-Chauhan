import requests

r = requests.get('https://docs.python-requests.org/en/latest/index.html')

print(r)  # <Response [200]> means okay

print(dir(r)) # attributes

# print(help(r))

with open('index.html','w') as wf:
    wf.write(r.text)   # content of page in unicode


with open('python.png','wb') as wf:
    image = requests.get('https://tse1.mm.bing.net/th/id/OIP.F6zpe51JtVhNufE1pU1ZKwHaHa?rs=1&pid=ImgDetMain&o=7&rm=3')
    wf.write(image.content)   # content of page in unicode
    print('status code: ',image.status_code)
    print('is okay?',image.ok)

print('Headers: ',r.headers)
print('server header', r.headers['Server'])
