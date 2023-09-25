from dataclasses import dataclass


@dataclass
class Endpoints:
    BASE_URL: str = 'https://employees-api-i9ae.onrender.com/'
    TOKEN_URL: str = BASE_URL + '/generate-token'
    EMPLOYEES_URL: str = BASE_URL + '/employees'
    EMPLOYEES_URL_ID: str = BASE_URL + '/employees' + '/1'