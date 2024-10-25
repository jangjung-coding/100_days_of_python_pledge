# What is API?
'''
An Application Programming Interface (API) is 
a set of rules and protocols that allows one software application to interact with another. 
In other words, an API is the messenger that delivers your request to the provider 
that you're requesting it from and then delivers the response back to you.
'''

# What is API endpoint?
'''
An API endpoint is a point at which an application program interface (API)
sends or receives information from a server.
'''

import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
print(response) # <Response [200]>
print(response.status_code) # 200

# Response Codes
'''
1XX: Hold on
2XX: Here you go
3XX: Go away
4XX: You screwed up
5XX: I screwed up
'''

