from json import loads, dumps
from django.http import HttpResponse

from django.core.serializers import serialize


class httpMixinResponnse(object):
    def render_to_json_response(self, data):
      
        return HttpResponse(data, content_type='application/json')
    
class MixinResponse(object):
    def render_to_pure_json_response(self, emp):
        data = serialize('json', emp, fields=('name', 'position', 'department'))
        q_data = loads(data)
        data_list = []
        for obj in q_data:
            obj_data = obj['fields']
            data_list.append(obj_data)
        data = dumps(data_list)
        return data