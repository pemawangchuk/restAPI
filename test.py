import requests
import json

BASEURL = "http://127.0.0.1:8000//"
ENDPOINT = "api/employee/list/"


url = (BASEURL + ENDPOINT)
id = input("Enter employee ID: ")

def test_employee_detail(id):
    response = requests.get(url+id+'/')
 
    data = response.json()
    
    
    if response.status_code == 200:
        print(response.status_code)
        print(json.dumps(data))
        

def test_employee_list():
    response = requests.get(url)
    
    data = response.json()
    
    if response.status_code == 200:
        print(response.status_code)
        print(json.dumps(data, indent=4))
    else:
        print("Failed to retrieve employee list. Status code:", response.status_code)

test_employee_list()