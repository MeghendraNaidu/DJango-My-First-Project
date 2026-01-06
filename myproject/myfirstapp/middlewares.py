

class Middleware1:
    def __init__(self, get_response):
        print("Middleware1 is initializing")
        self.get_response = get_response
        
    def __call__(self, request):
        if request.path == "/home/":
            print("Middleware1 is accpting request")
        response = self.get_response(request)
        return response
    
class Middleware2:
    def __init__(self, get_response):
        print("Middleware2 is initializing")
        self.get_response = get_response
        
    def __call__(self, request):
        if request.path == "/about/":
            print("Middleware2 is accpting request")
        response = self.get_response(request)
        return response