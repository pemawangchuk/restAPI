from django.http import HttpResponse
from django.shortcuts import render

from app.models import Employee



# Create your views here.

def home(request):
    data = {
        "message": "Welcome to the API Home!",
        "status": "success"
    }

    resp = 'message:{}, status:{}'.format(data['message'], data['status'])

    return HttpResponse("Welcome to the  Home!", resp)

from json import dumps, loads
def api_home(request):
    data = {
        "message": "Welcome to the API Home!",
        "status": "success"
    }
    resp = dumps(data)
    
    return HttpResponse(resp, content_type='application/json')


from django.views.generic import View
from app.mixin import MixinResponse, httpMixinResponnse

class HomeView(httpMixinResponnse, View):
    def get(self, request, *args, **kwargs):
        data = {
        "message": "Welcome to the API Home!",
        "status": "success"
        }
        resp = dumps(data) 
        
        return self.render_to_json_response(resp)
    


class EmployeeDetail(httpMixinResponnse, View):
    def get(self, request, id, *args, **kwargs):
        emp = Employee.objects.get(id = id)

        employee_data = {
            "name": emp.name,
            "position": emp.position,
            "department": emp.department
        }

        emp = dumps(employee_data)
        return self.render_to_json_response(emp)
        
from django.core.serializers import serialize


class EmployeeDetailSerializer(httpMixinResponnse, View):
    def get(self, request, id, *args, **kwargs):
        emp = Employee.objects.get(id=id)
        employee_data = serialize('json', [emp,], fields=('name', 'position', 'department'))

        q_data = loads(employee_data)
        data_list =[]

        for obj in q_data:
            obj_data = obj['fields']
            data_list.append(obj_data)

        employee_data = dumps(data_list)
        
        return HttpResponse(employee_data, content_type="application/json")
    
class EmployeeListSerializer(MixinResponse, View):
    def get(self, request, *args, **kwargs):
        emp = Employee.objects.all()
        employee_data = self.render_to_pure_json_response(emp)
        
        return HttpResponse(employee_data)

    