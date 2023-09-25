import requests


class Employees:
    def __init__(self, url: str, session: requests.Session, token):
        self.session = session
        self.url = url
        self.token = token
        self.json_data = {
            "name": "Sergey",
            "organization": "Advertising",
            "role": "Advertiser"
        }
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        self.json_update = {
            "name": "Mikhail",
            "organization": "Accounting",
            "role": "Consultant"
        }

    def fetch_all_employees(self):
        response = self.session.get(self.url, headers=self.headers)
        assert response.status_code == 200, f'status code is incorrect: {response.status_code}'


    def create_employee(self):
        response = self.session.post(self.url, headers=self.headers, json=self.json_data)
        assert response.status_code == 200, f'status code is incorrect: {response.status_code}'
        assert response.json()['name'] == 'Sergey'
        assert response.json()['organization'] == 'Advertising'


    def update_employee(self):
        response = requests.put(self.url, headers=self.headers)
        assert response.status_code == 200, f'status code is incorrect: {response.status_code}'
        assert response.json()['message'] == 'Employee updated'


    def delete_employee(self):
        response = requests.delete(self.url, headers=self.headers)
        assert response.status_code == 201, f'status code is incorrect: {response.status_code}'
        assert response.json()['message'] == 'Employee deleted'


    def fetch_single_employee(self, emp_id, data):
        response = self.session.get(self.url + emp_id, headers=self.headers)
        assert response.json() == data, f"FAILED. Actual data: {response.json()} but need: {data}"


