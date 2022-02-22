import urllib.request

while(True):
     with urllib.request.urlopen('http://localhost') as response:
          html = response.read()
