from django.utils.deprecation import MiddlewareMixin

class mymiddle(MiddlewareMixin):
    def process_request(self, request):
        print("get :",request.GET.get("a"))