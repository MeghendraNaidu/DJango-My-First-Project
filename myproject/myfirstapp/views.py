from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import math
from django.views.decorators.csrf import csrf_exempt


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

# def stu_info(request):
#     info = {"Data" : [{"Name" : "Meghendra", "Age" : 22, "Gender" : "Male", "City": "Hyd"}, 
#                     {"Name" :"Nickel", "Age" : 21, "Gender" : "Male", "City": "Ban"}, 
#                     {"Name" : "NagaRaju", "Age" : 23, "Gender" : "Male", "City" : "Hyd"},
#                     {"Name" : "Ramanji", "Age" : 22, "Gender" : "Male", "City" : "Ban"}]}
#     filterData = []
#     city = request.GET.get("city", "Hyd")
    
#     for i in info:
#         if i["City"] == city:
#             filterData.append(i)
#     return JsonResponse(filterData)

# def pagination(request):
#     data=['apple','banana','carrot','grapes','watermelon','kiwi','pineapple','custard-apple','strawberry','blueberry','dragonfruit']
#     page=int(request.GET.get("page",1))
#     limit=int(request.GET.get("limit",3))

#     start=(page-1)*limit
#     end=page*limit
#     total_pages=math.ceil(len(data)/limit)
#     result=data[start:end]

#     res={"status":"success","current_page":page,"total_pages":total_pages,"data":result}
#     return JsonResponse(res,status=302)

# student_info = [{"id":"1", "Name":"Meghendra", "Degree":"CSE"}]

# 26-12-2025
# @csrf_exempt


# 27-12-2025
