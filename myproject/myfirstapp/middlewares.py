import json
from django.http import JsonResponse


# 06-1-2026
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
    
# 07-1-2026
# Midlleware we can use for many putposes
# 1. validation
# 2. data encryption
# 3. data formatting and cleaning
class SSCStatusMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.path in ["/job1/", "/job2/"] and request.method == "POST":
            incoming_data = json.loads(request.body)
            ssc_status = incoming_data.get("ssc_status")
            if not ssc_status:    
                return JsonResponse({"Status" : "Failure", "Message" : "U Need to Qualify the SSC"})
        # return self.get_response(request)
        response = self.get_response(request)
        return response
        
class MedicallyFitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.path == "/job1/" and request.method == "POST":
            incoming_data = json.loads(request.body)
            medical_fit = incoming_data.get("medical_fit")
            if not medical_fit:    
                return JsonResponse({"Status" : "Failure", "Message" : "U Should Medically Fit To Apply This Job"})
        # return self.get_response(request)
        response = self.get_response(request)
        return response
        
class AgeValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.path in ["/job1/", "/job2/"] and request.method == "POST":
            incoming_data = json.loads(request.body)
            age = incoming_data.get("age")
            if age <= 21:    
                return JsonResponse({"Status" : "Failure", "Message" : "U Should Have Atleast More Then 21 Years To Apply This Job"})
        # return self.get_response(request)
        response = self.get_response(request)
        return response
    
class IntermediateStatusMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.path in ["/enginaaringseat/"] and request.method == "POST":
            incoming_data = json.loads(request.body)
            inter_status = incoming_data.get("inter_status")
            if inter_status <= 800:    
                return JsonResponse({"Status" : "Failure", "Message" : "U Need to Qualify the Intermediate To Get Engineering Seat"})
        # return self.get_response(request)
        response = self.get_response(request)
        return response
    
class EamcetStatusMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.path in ["/enginaaringseat/"] and request.method == "POST":
            incoming_data = json.loads(request.body)
            eamcet_status = incoming_data.get("eamcet_status")
            if eamcet_status <= 40:    
                return JsonResponse({"Status" : "Failure", "Message" : "U Need to Qualify the Eamcet To Get Engineering Seat"})
        # return self.get_response(request)
        response = self.get_response(request)
        return response