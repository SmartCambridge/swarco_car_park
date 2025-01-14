from urllib import request
import json

api_url = "https://sso.swarco.com/auth/realms/swarco/protocol/openid-connect/token",
# headers={"Content-Type": "application/x-www-form-urlencoded"}

req = request.Request(api_url, method="POST")
req.add_header('Content-Type', 'application/json')
data = {
    'grant_type': 'password',
    'client_id': 'swarco.ui.base',
    'username': 'cambridge_smi@swarco.com',
    'password': 'sNeX1Hxm2H'
}

data = json.dumps(data)
data = data.encode()
r = request.urlopen(req, data=data)
content = r.read()
print(content)