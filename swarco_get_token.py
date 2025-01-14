import requests
import json

api_url = "https://sso.swarco.com/auth/realms/swarco/protocol/openid-connect/token"
post_headers={
    'Content-Type': 'application/x-www-form-urlencoded'
}

obj_data = {
    'grant_type': 'password',
    'client_id': 'swarco.ui.base',
    'username': 'cambridge_smi@swarco.com',
    'password': 'sNeX1Hxm2H'
}

api_data = 'grant_type = "password"\nclient_id="swarco.ui.base"\nusername="cambridge_smi@swarco.com"\npassword="sNeX1Hxm2H"\n'

#str_data = json.dumps(api_data)
#send_data = str_data.encode()

r = requests.post(api_url, data=obj_data, headers=post_headers)
content = r.text
status = r.status_code
print(content)
