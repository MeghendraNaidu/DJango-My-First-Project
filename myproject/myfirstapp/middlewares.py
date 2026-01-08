import json
from django.http import JsonResponse
# from .validations import validate_username, validate_email, validate_password
import re


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
    
USERNAME_REGEX = re.compile(r'^[a-zA-Z][a-zA-Z0-9_]{4,19}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
PASSWORD_REGEX = re.compile(
    r'^(?=(?:.*[A-Z]){2})(?=(?:.*[a-z]){2})(?=(?:.*\d){2})(?=(?:.*[#@$!%*?&]){2})[A-Za-z\d#@$!%*?&]{8,}$'
)

def validate_username(username):
    return bool(USERNAME_REGEX.match(username))

def validate_email(email):
    return bool(EMAIL_REGEX.match(email))

def validate_password(password):
    return bool(PASSWORD_REGEX.match(password))

class UserNameValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.path == "/usersignup/" and request.method == "POST":
            data = json.loads(request.body)
            username = data.get("username")
            if not validate_username(username):
                return JsonResponse({"Status" : "Failure", "Message" : "Please Enter the Valid UserName"})
        response = self.get_response(request)
        return response

class UserEmailValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.path == "/usersignup/" and request.method == "POST":
            data = json.loads(request.body)
            useremail = data.get("email")
            if not validate_email(useremail):
                return JsonResponse({"Status" : "Failure", "Message" : "Please Enter the Valid Email"})
        response = self.get_response(request)
        return response

class UserPasswordValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.path == "/usersignup/" and request.method == "POST":
            data = json.loads(request.body)
            userpassword = data.get("password")
            if not validate_password(userpassword):
                return JsonResponse({"Status" : "Failure", "Message" : "Please Enter the Valid And Strong Password"})
        response = self.get_response(request)
        return response