import requests

url = "https://api.hh.ru/token"
payload = {
    'grant_type': 'authorization_code',
    'client_id': 'IOC0UP207LQLRF0B0VELDH73D2C8J0CHK3RR353KDRSMJ6B54VJE4J4SCV0LDN3S',
    'client_secret': 'G742S2A66RBRTQD4E67OFKL0GATHVSGA3PPDASP82T2D05E1QHJVK6IRPTM9NQV9',
    'redirect_uri' = 'http://localhost',
    'code': 'RIPUKGILGC1DJHIJ785MA7RUEDF13JBA2112MTEGAMO201COGI42AE393AO4A06O'
}

response = requests.post(url, data=payload)
print(response.json())
