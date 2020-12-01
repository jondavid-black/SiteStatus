import requests

urls = [
    'https://www.google.com',
    'https://www.github.com',
    'https://devopsfordefense.org',
    'https://www.github.com/jondavid-black/notapage.html',
    'https://notasite.com'
]

response = []

for url in urls :
    try:
        r = requests.get(url)
        response.append((url, r.status_code))
    except:
        response.append((url, 'error'))

for entry in response:
    print(entry)
