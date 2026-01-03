from django.shortcuts import render
from django.http import JsonResponse
from .models import OrderDetails, MovieBooking, BookDetails
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
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
        
        
        