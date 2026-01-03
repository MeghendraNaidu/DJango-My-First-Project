from django.shortcuts import render
from django.http import JsonResponse
from .models import OrderDetails, MovieBooking, BookDetails
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def GetOrders(request):
    try:
        if request.method=="GET":
            result=list(OrderDetails.objects.values()) #to get all the records from the table
            print(result)
            if len(result)==0:
                msg="No records found"
            else:
                msg="Data retrieved successfully"
            return JsonResponse({"status":"success","message":msg,"data":result,"total no.of records":len(result)})
        return JsonResponse({"status":"failure","message":"only get method allowed"})
    except Exception as e:
        return JsonResponse({"message":"something went wrong"})
    
@csrf_exempt
def orderPlacing(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            order=OrderDetails.objects.create(orderid=data["order_id"], useremail=data["email"], amount=data["amount"], status=data["status"], mode=data["mode"])
            print(order.transaction_id)
            x=order.transaction_id
            return JsonResponse({"status":"success", "message":"payment details updated successfully", "transaction_id":x },status=201)
        else:
            return JsonResponse({"error":"only post method is allowed"},status=400)
    except Exception as e:
        print(e)
        return JsonResponse({"error":"something went wrong"},status=500)
    
# task on 20-12-2025:
# ------
# practise this
# create an api to book a movie ticket. with fields-->moviename,showtime,screenname,dateandtime,transcationid.

@csrf_exempt
def BookMyshow(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            MovieBooking.objects.create(moviename=data["movie_name"],
            showtime=data["show_time"],screenname=data["screen_name"])
            return JsonResponse({"status":"success","msg":"records inserted successfully"})
        return JsonResponse({"status":"failure","message":"only post method allowed"})
    except Exception as e:
        return JsonResponse({"message":"something went wrong"})

@csrf_exempt
def BookingDetails(request):
    try:
        if request.method=="GET":
            result=list(MovieBooking.objects.values())
            if len(result)==0:
                msg="No records found"
            else:
                msg="Data retrieved successfully"            
            return JsonResponse({"status":"success","message":msg,"data":result,"total no.of records":len(result)})
        return JsonResponse({"status":"failure","message":"only get method allowed"})
    except Exception as e:
        return JsonResponse({"message":"something went wrong"})
    
student_info=[{"id":1,"name":"vasanth","degree":"EEE"},
{"id":2,"name":"krishna","degree":"ECE"},
{"id":3,"name":"kiran","degree":"CSE"},
{"id":4,"name":"Anvesh","degree":"EEE"}]

def getStudentById(request,id):
    filteredStudent=[]

    for student in student_info:
        if id==student["id"]:
            filteredStudent.append(student)

    return JsonResponse({"data":filteredStudent})

@csrf_exempt
def getStudentsByDegree(request,deg):
    try:
        if request.method=="GET":
            DegreeBasedFilteration=[]
            for student in student_info:
                if deg.lower()== student["degree"].lower():
                    DegreeBasedFilteration.append(student)
            if len(DegreeBasedFilteration)==0:
                msg="no records found"
            else:
                msg="students record fetched successfully"
            return JsonResponse(
                {"status":"success",
                "no.of records":len(DegreeBasedFilteration),
                "data":DegreeBasedFilteration,
                "msg":msg
                },status=200)
        return JsonResponse({"status":"failure","message":"only get method is allowed"},status=400)
    except Exception as e:
        return JsonResponse({"status":"error","msg":"something went wrong, check the code once"})
    
#if we are expecting only single record is available
def getOrdersByStatus(request,status_param):
    try:
        if request.method=="GET":
            data=OrderDetails.objects.get(status=status_param) #it will works if we have only single object 
            print(data.orderid)
            print(data.mode)
            ResponseObject={"id":data.orderid,"amount":data.amount,"mode":data.mode}
            return JsonResponse({"status":"success","msg":"records fetched successfully","data":ResponseObject},status=200)
        return JsonResponse({"status":"failure","msg":"only get method is allowed"},status=400)
    except Exception as e:
        return JsonResponse({"status":"error","msg":"something went wrong"},status=500)


#if we are expecting multiple records based on filteration

def getMultiplesOrdersByStatus(request,status):
    try:
        if request.method=="GET":
            print(status)

            data=(OrderDetails.objects.filter(status=status))
            final=list(data.values("id","useremail","orderid","amount","currency","transaction_id")) 
            if len(final)==0:
                msg="no records found"
            else:
                msg="records fetched successfully"
            return JsonResponse({"status":"success","no.of records":len(final),"msg":msg,"data":final},status=200)
        return JsonResponse({"status":"failure","msg":"only get method is allowed"},status=400)
    except Exception as e:
        return JsonResponse({"status":"error","msg":"something went wrong"},status=500)

def getMoviesByScreenname(request,screen):
    try:
        if request.method=="GET":
            data=MovieBooking.objects.filter(screenname=screen).values()           
            final_data=list(data) 
            if len(final_data)==0:
                msg="no records found"
            else:
                msg="Records fetched successfully"          
            return JsonResponse({"status":"success","msg":msg,screen:final_data},status=200)
        return JsonResponse({"status":"failure","msg":"only get method allowed"},status=400)
    except Exception as e:
        return JsonResponse({"status":"error","msg":"something went wrong"})

        
def getMoviesByMultipleScreens(request,first,second):
    try:
        if request.method=="GET":
            data1=MovieBooking.objects.filter(screenname=first).values()
            data2=MovieBooking.objects.filter(screenname=second).values()
            first_data=list(data1)
            second_data=list(data2)            
            return JsonResponse({"status":"success",first:first_data,second:second_data},status=200)
        return JsonResponse({"status":"failure","msg":"only get method allowed"},status=400)
    except Exception as e:
        return JsonResponse({"status":"error","msg":"something went wrong"})

@csrf_exempt
def updateOrderStatus(request,ref_status):
    try:
        if request.method=="PUT":
            input_data=json.loads(request.body)
            new_status=input_data["new_status"]
            update=OrderDetails.objects.filter(status=ref_status).update(status=new_status)
            if update==0:
                msg="no record found with referrence of id"
            else:
                msg="record is updated successfully"
            return JsonResponse({"status":"success","msg":msg},status=200)
        return JsonResponse({"status":"failure",":msg":"only put method is allowed"},status=400)
    except Exception as e:
        return JsonResponse({"status":"error","message":"something went wrong"},status=500)


#update screen4 to screen1 in moviebooking table
    
@csrf_exempt
def UpdateScreenByScreen(request,ref_screen):
    try:
        if request.method == "PUT":
            input_data = json.loads(request.body)
            new_screen = input_data["screen_name"]
            update = MovieBooking.objects.filter(screenname = ref_screen).update(screenname = new_screen)
            if update == 0:
                msg = "No Record Found"
            else:
                msg = "Record Updated Successfully"
            return JsonResponse({"status" : "success","msg" : msg},status = 200)
        return JsonResponse({"status" : "failure","msg" : "only PUT method allowed"},status = 400)
    except Exception as e:
        return JsonResponse({"status" : "error","msg" : "something went wrong"}, status = 500)

# 31-12-2025
@csrf_exempt
def AddBookDetails(request):
    try:
        if request.method == "POST":
            input_data = json.loads(request.body)
            BookDetails.objects.create(Book_Name = input_data["Book_Name"], Book_Author = input_data["Book_Author"], Book_Price = input_data["Book_Price"], Book_Type = input_data["Book_Type"])
            return JsonResponse({"status" : "Success", "msg" : "Record Added Successfully"}, status = 200)
        return JsonResponse({"status" : "failure", "msg" : "Only POST Method is Allowed"}, status = 400)
    except Exception as e:
        return JsonResponse({"status" : "Error", "msg" : "Somthing Went Wrong"}, status = 500)
    
@csrf_exempt
def GetBooksDetails(request):
    try:
        if request.method == "GET":
            Get_Books = list(BookDetails.objects.values())
            if len(Get_Books) == 0:
                msg = "No Record Found"
            else:
                msg = "Data Retrieved Successfully"
            return JsonResponse({"status" : "Success", "msg" : msg, "Records" : Get_Books}, status = 200)
        return JsonResponse({"status" : "Failure", "msg" : "Only GET method is Allowed"}, status = 400)
    except Exception as e:
        return JsonResponse({"status" : "Error", "msg" : "Something Went wrong"}, status = 500)
    
@csrf_exempt
def UpdateBookDetails(request, ref_id):
    try:
        if request.method == "PUT":
            input_data = json.loads(request.body)
            New_Book_Type = input_data["Book_Type"]
            update = BookDetails.objects.filter(id = ref_id).update(Book_Type = New_Book_Type)
            if update == 0:
                Message = "No Record Found"
            else:
                Message = "Record Updated Successfully"
            return JsonResponse({"Status" : "Success", "Message" : Message}, status = 200) 
        return JsonResponse({"Status" : "Failure", "Message" : "Only PUT Method is Allowed"}, status = 400)
    except Exception as e:
        return JsonResponse({"Status" : "Error", "Message" : "Something Went Wrong"}, status = 500)
    
@csrf_exempt
def DeleteBookDetails(request, ref_id):
    try:
        if request.method == "DELETE":
            delete = BookDetails.objects.filter(id = ref_id).delete()
            if delete[0] == 0:
                Message = "No Record Found"
            else:
                Message = "Record Updated Successfully"
            return JsonResponse({"Status" : "Success", "Message" : Message}, status = 200) 
        return JsonResponse({"Status" : "Failure", "Message" : "Only DELETE Method is Allowed"}, status = 400)
    except Exception as e:
        return JsonResponse({"Status" : "Error", "Message" : "Something Went Wrong"}, status = 500)
    
@csrf_exempt
def MethodsOnBookDetails(request):
    try:
        
        if request.method == "POST":
            input_data = json.loads(request.body)
            BookDetails.objects.create(Book_Name = input_data["Book_Name"], Book_Author = input_data["Book_Author"], Book_Price = input_data["Book_Price"], Book_Type = input_data["Book_Type"])
            return JsonResponse({"Status" : "Success", "Message" : "Record Inserted Successfully"}, status = 200)
        
        elif request.method == "GET":
            Get_Books = list(BookDetails.objects.values())
            if len(Get_Books) == 0:
                Message = "No Record Found"
            else:
                Message = "Records  Retrived Successfully"
            return JsonResponse({"Status" : "Success", "Message" : Message, "Result" : Get_Books}, status =200)
        
        elif request.method == "PUT":
            input_data = json.loads(request.body)
            update = BookDetails.objects.filter(id = input_data["id"]).update(Book_Type = input_data["Book_Type"])
            if update == 0:
                Message = "No Record Found"
            else:
                Message = "Record Updated Successfully"
            return JsonResponse({"Status" : "Success", "Message" : Message}, status =200)
        
        elif request.method == "DELETE":
            input_data = json.loads(request.body)
            delete = BookDetails.objects.filter(id = input_data["id"]).delete()
            if delete[0] == 0:
                Message = "No Record Found"
            else:
                Message = "Record Deleted Successfully"
            return JsonResponse({"Status" : "Success", "Message" : Message}, status =200)
        
        else:
            return JsonResponse({"Status" : "Failure", "Message" : "Please Enter the Valid HTTP Method"}, status =405)
        
    except Exception as e:
        return JsonResponse({"Status" : "Error", "Message" : "Something Went Wrong Please Check Once Again"}, status = 500)
        
        
        