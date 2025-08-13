from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.

def home(request):
    data = {
        "message": "Welcome to the API Home!",
        "status": "success"
    }

    resp = 'message:{}, status:{}'.format(data['message'], data['status'])

    return HttpResponse("Welcome to the  Home!", resp)

from json import dumps
def api_home(request):
    data = {
        "message": "Welcome to the API Home!",
        "status": "success"
    }
    resp = dumps(data)
    
    return HttpResponse(resp, content_type='application/json')


from django.views.generic import View
from app.mixin import httpMixinResponnse

class HomeView(httpMixinResponnse, View):
    def get(self, request, *args, **kwargs):
        data = {
        "message": "Welcome to the API Home!",
        "status": "success"
        }
        resp = dumps(data) 
        
        return self.render_to_json_response(resp)
    

    