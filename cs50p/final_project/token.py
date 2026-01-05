import requests

url = "https://api.hh.ru/token"
payload = {
    'grant_type': 'authorization_code',
    'client_id': 'IOC0UP207LQLRF0B0VELDH73D2C8J0CHK3RR353KDRSMJ6B54VJE4J4SCV0LDN3S',
    'client_secret': 'G742S2A66RBRTQD4E67OFKL0GATHVSGA3PPDASP82T2D05E1QHJVK6IRPTM9NQV9',
    'redirect_uri': 'http://localhost',
    'code': 'RIPUKGILGC1DJHIJ785MA7RUEDF13JBA2112MTEGAMO201COGI42AE393AO4A06O'
}

response = requests.post(url, data=payload)
print(response.json())

# {
#     'access_token': 'USERTUNGS70TSFPSNLDLS1PKIEM4GE2CCA51OI6F5UCK31UI476IJ7SBESK7AMQT',
#     'token_type': 'bearer',
#     'refresh_token': 'USERN8EUN6EUMRFL8CJMNCSDSFFTJ23F7JQDF5AIJ3JTO4S2QH9ELHFQ7G95MH8T',
#     'expires_in': 1209599
#  }
