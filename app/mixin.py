from django.http import HttpResponse

class httpMixinResponnse(object):
    def render_to_json_response(self, data):
      
        return HttpResponse(data, content_type='application/json')