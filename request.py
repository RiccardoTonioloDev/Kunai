import requests
import string

#IP 

ip = "127.0.0.1"
port = "8080"

#Request Cookies
for i in range(100):
    cookies = {'name': 'value'}
    r = requests.post(f"http://{ip}:{port}", cookies)
    r.cookies  # Where "FLAG" is another cookies's name and this return the cookies FLAG value

#Request Headers
stringa='valore'
r = requests.get(ip, headers={'Accept-Language':stringa})

for i in string.ascii_letters:
    url = f"http://127.0.0.1:124/?pass={i}"
    r = requests.get(url, headers={'User-Agent': str(i)})
    print(r.text)


#HashLib
