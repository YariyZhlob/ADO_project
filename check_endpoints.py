import requests


API_URL = 'http://127.0.0.1:5000/employees'
BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InN1cGVydXNlciJ9.TFbOhuR_QuXdrgYCLHOXibp_OW_ZNGgsozTo0130dVw'

headers = {'Authorization': f'Bearer {BEARER_TOKEN}', 'Content-Type': 'application/json'}

data = {
        "name": "Sergey",
        "organization": "Advertising",
        "role": "Advertiser"
}

response = requests.post(url=API_URL, headers=headers,json=data)

print(response.status_code)
print(response.json())

def test_new_employee_creation():
        print(response.status_code)
        assert response.json()['name'] == 'Sergey'
        assert response.json()['organization'] == 'Advertising'