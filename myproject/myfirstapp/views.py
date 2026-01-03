from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import math
import json
from django.views.decorators.csrf import csrf_exempt
from myfirstapp.models import userProfile,Employee
from django.db.utils import IntegrityError


# Create your views here.
# 05-12-2025
def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def services(request):
    return render(request, "services.html")

# 09-12-2025 on this date we discuss about the deployment to git and render

# 10-12-2025
def sample(request):
    print(request)
    qp1=request.GET.get("name")
    qp2=request.GET.get("city")
    return HttpResponse(f"{qp1} is from {qp2}")

def sample1(request):
    info={"data":[{"name":"akanksha","city":"hyd","gender":"female"},
                  {"name":"uma","city":"bnglr","gender":"female"},
                  {"name":"durgaprasad","city":"vij","gender":"male"}]}
    return JsonResponse(info)

# 11-12-2025
#dynamic response using query params
def productInfo(request):
    product_name=request.GET.get("product",'mobile')
    quantity=int(request.GET.get("quantity",1))
    price=int(request.GET.get("price",25000))
    data={"product":product_name,"quantity":quantity,"price":price,"totalprice":price*quantity}
    return JsonResponse(data)

#filtering using query params
def filteringData(request):
    data=[1,2,3,4,5,6,7,8,9,10]
    filteredData=[]
    qp=int(request.GET.get("num",2))
    for x in data:
        if x%qp==0:
            filteredData.append(x)
    return JsonResponse({"data":filteredData})

students_data=[{'name':'durgaprasad','city':'hyd'},
               {'name':'rajendra','city':'hyd'},
               {'name':'uma','city':'bnglr'},
               {'name':'kiran','city':'bnglr'}]

def filterStudentsByCity(request):
    filteredStudents=[]
    city=request.GET.get("city","hyd")

    for student in students_data:
        if student["city"]==city:
            filteredStudents.append(student)
    return JsonResponse({"status":"success","data":filteredStudents})

# response={"status":"success","pagenum":2,"limit":4,"total_pages":4,"data":[{},{},{}]}

# 13-12-2025
def pagination(request):
    data=['apple','banana','carrot','grapes','watermelon','kiwi','pineapple','custard-apple','strawberry','blueberry','dragonfruit']
    page=int(request.GET.get("page",1))
    limit=int(request.GET.get("limit",3))

    start=(page-1)*limit
    end=page*limit
    total_pages=math.ceil(len(data)/limit)
    result=data[start:end]

    res={"status":"success","current_page":page,"total_pages":total_pages,"data":result}
    return JsonResponse(res,status=302)

# python manage.py shell -c "from django.db import connection; c=connection.cursor(); c.execute('SELECT DATABASE(), VERSION()'); print(c.fetchone())"
# This command is used check if the db connection is done or not

# 17-12-2025
# Here POST method is used without database
@csrf_exempt
def createData(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
    return JsonResponse({"status":"success","data":data,"statuscode":201})

@csrf_exempt
def createProduct(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
    return JsonResponse({"status":"success","data":data,"statuscode":201})

# Here POST method is used with database
@csrf_exempt
def createDataToDB(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body) #dictionary
            name=data.get("name") #taking name property from dict
            age=data.get("age") #taking age property from dict
            city=data.get("city") #taking city property from dict
            userProfile.objects.create(name=name,age=age,city=city)
            print(data)
        return JsonResponse({"status":"success","data":data,"statuscode":201},status=201)
    
    except Exception as e:
        return JsonResponse({"statuscode":500,"message":"internal server error"})
    
@csrf_exempt
def createEmployee(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            print(data)
            Employee.objects.create(emp_name=data.get("name"),emp_salary=data.get("sal"),emp_email=data.get("email"))
        return JsonResponse({"status":"success","data":data,"statuscode":201},status=201)
    except IntegrityError as e:        
        return JsonResponse({"status":"error","message":"inputs are invalid or not acceptable"},status=400)
    finally:
        print("done")
        
# Todays Task is
# create product model with fields produ_name,price and quantity,totalprice


# student_info = [{"id":"1", "Name":"Meghendra", "Degree":"CSE"}]

# 26-12-2025
# @csrf_exempt


# 27-12-2025

# 30-12-2025
@csrf_exempt       
def UpdateUserCityById(request):
    try:
        if request.method=="PUT":
            input_data=json.loads(request.body)
            ref_id=input_data["id"]
            new_city=input_data["new_city"]
            update=userProfile.objects.filter(id=ref_id).update(city=new_city)
            if update==0:
                msg="no record found"
            else:
                msg="record updated"
            print(update)
            return JsonResponse({"status":"success","msg":msg},status=200)
        return JsonResponse({"status":"failure",":msg":"only put method is allowed"},status=400)
    except Exception as e:
         return JsonResponse({"status":"error","message":"something went wrong"},status=500)

@csrf_exempt
def updateUseragebyId(request):
    try:
        if request.method=="PUT":
            input_data=json.loads(request.body)
            ref_id=input_data["id"]
            new_age=input_data["new_age"]
            update=userProfile.objects.filter(id=ref_id).update(age=new_age)
            if update==0:
                msg="no record found with referrence of id"
            else:
                msg="record is updated successfully"
            return JsonResponse({"status":"success","msg":msg},status=200)
        return JsonResponse({"status":"failure",":msg":"only put method is allowed"},status=400)
    except Exception as e:
        return JsonResponse({"status":"error","message":"something went wrong"},status=500)
@csrf_exempt
def DeleteUserById(request,ref_id):
    try:
        if request.method=="DELETE": 
            delete=userProfile.objects.filter(id=ref_id).delete() 
            print(delete[0])  
            if delete[0]==0:
                msg="no record is found to delete"
            else:
                msg="record is deleted successfully"        
            return JsonResponse({"status":"success","msg":msg},status=200)
        return JsonResponse({"status":"failure",":msg":"only DELETE method is allowed"},status=400)
    except Exception as e:
        return JsonResponse({"status":"error","message":"something went wrong"},status=500)
