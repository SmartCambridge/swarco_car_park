import requests
import json

token_url = "https://sso.swarco.com/auth/realms/swarco/protocol/openid-connect/token"
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

r = requests.post(token_url, data=obj_data, headers=post_headers)
content = r.text
status = r.status_code
#print(content)

return_data = r.json()

print("## Get token")
print("https://sso.swarco.com/auth/realms/swarco/protocol/openid-connect/token")

print(return_data)

access_token = return_data['access_token']

get_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+access_token
}

url_cam_dynamic = 'https://mycity.swarco.com/api/swarco.pgs.smi.v8/getDynamicPOIDataByPgs/CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2'

url_cam_static = 'https://mycity.swarco.com/api/swarco.pgs.smi.v8/getStaticPOIDataByPgs/CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2'

working_car_parks_url = "https://mycity.swarco.com/api/swarco.pgs.smi.v8/getDynamicPOIDataByPgs/CLD_PGS_d4cca5b5-5903-41bb-bfb0-fbec919c42fb"

#r = requests.get(working_car_parks_url, headers=get_headers)
r = requests.get(url_cam_dynamic, headers=get_headers)
print("## Get Dynamic data")
print('https://mycity.swarco.com/api/swarco.pgs.smi.v8/getDynamicPOIDataByPgs/CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2')
print(r.text)

r = requests.get(url_cam_static, headers=get_headers)

print("## Get Static data")
print('https://mycity.swarco.com/api/swarco.pgs.smi.v8/getStaticPOIDataByPgs/CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2')
print(r.text)
