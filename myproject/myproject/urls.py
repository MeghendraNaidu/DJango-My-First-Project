"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myfirstapp.views import protected_api, login, signup, UserSignUp, Engineering_Seat, job2, job1, DeleteUserById, updateUseragebyId, UpdateUserCityById, createEmployee, createDataToDB, createProduct, createData, pagination, filterStudentsByCity, filteringData, productInfo, sample1, sample, home, about, contact, services

from mysecondapp.views import MethodsOnBookDetails, DeleteBookDetails, UpdateBookDetails, GetBooksDetails, AddBookDetails, updateOrderStatus, UpdateScreenByScreen, getMoviesByMultipleScreens, getMoviesByScreenname, getMultiplesOrdersByStatus, getOrdersByStatus, getStudentsByDegree, getStudentById, BookingDetails, GetOrders, BookMyshow, orderPlacing

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", home, name = "home"),
    path("about/", about, name = "about"),
    path("contact/",contact, name = "contact"),
    path("services/", services, name = "services"),
    path('sample/',sample),
    path('sample1/',sample1),
    path('product/',productInfo),
    path('filter/',filteringData),
    path('students/',filterStudentsByCity),
    path('pagination/',pagination),
    path('create/',createData),
    path('productcreate/',createProduct),
    path('createuser/', createDataToDB),
    path('emp/',createEmployee),
    path('order/',orderPlacing),
    path('bookticket/',BookMyshow),
    path('getOrders/',GetOrders),
    path('getBookings/',BookingDetails),
    path('getStudent/<int:id>',getStudentById),
    path('getStudentsByDegree/<str:deg>',getStudentsByDegree),
    path('orderByStatus/<str:status_param>',getOrdersByStatus),
    path('orders/<str:status>',getMultiplesOrdersByStatus),
    path('movieByScreen/<str:screen>',getMoviesByScreenname),
    path('movieByScreens/<str:first>/<str:second>',getMoviesByMultipleScreens),
    path('updatescreen/<str:ref_screen>',UpdateScreenByScreen),
    path('addbookdetails/', AddBookDetails),
    path('getbooks/', GetBooksDetails),
    path('updatebook/<str:ref_id>', UpdateBookDetails),
    path('deletebook/<str:ref_id>', DeleteBookDetails), 
    path('methodsonbook/', MethodsOnBookDetails),
    path('updateCity/',UpdateUserCityById),
    path('updateAge/',updateUseragebyId),
    path('deleteUser/<int:ref_id>',DeleteUserById),
    path('updateStatus/<str:ref_status>',updateOrderStatus),
    path('job1/', job1), 
    path('job2/', job2),
    path("enginaaringseat/", Engineering_Seat),
    path("usersignup/", UserSignUp),
    path("signup/",signup),
    path("login/",login),
    path('protect/',protected_api),
]
