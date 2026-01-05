import requests

url = "https://api.hh.ru/token"
payload = {
    'grant_type': 'authorization_code',
    'client_id': 'IOC0UP207LQLRF0B0VELDH73D2C8J0CHK3RR353KDRSMJ6B54VJE4J4SCV0LDN3S',
    'client_secret': 'G742S2A66RBRTQD4E67OFKL0GATHVSGA3PPDASP82T2D05E1QHJVK6IRPTM9NQV9',
    'redirect_uri' = 'JobAnalyzer://auth',
    'code': 'CODE_FROM_REDIRECT',  # The code received after user approval
    # 'redirect_uri': 'YOUR_REDIRECT_URI' # Optional, must match app settings
    grant_type=authorization_code
    client_id=ETVQdMs2n9VKw7SMXkh9nX5H
    client_secret=95dNjB8FmtxQsmygm6dtEy53&
    redirect_uri=http%3A%2F%2Fwww.example.com%2Foauth&
    code=29CtxMcaA8pRFDYyC8e8Gkm4

}

response = requests.post(url, data=payload)
print(response.json())
