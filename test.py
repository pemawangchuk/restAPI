import requests
import json

BASEURL = "http://127.0.0.1:8000//"
ENDPOINT = "api/employee/"

url = (BASEURL + ENDPOINT)
id = input("Enter employee ID: ")

def test_employee_detail(id):
    response = requests.get(url+id+'/')
 
    data = response.json()
    
    
    if response.status_code == 200:
        print(response.status_code)
        print(json.dumps(data))
        
test_employee_detail(id)