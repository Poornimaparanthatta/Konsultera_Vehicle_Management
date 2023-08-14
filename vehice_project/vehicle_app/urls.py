from django.urls import path
from vehicle_app import views

urlpatterns=[
       path('demo/',views.demo,name="demo"),
       path('addDetails/',views.addDetails,name="addDetails"),
       path('saveDetails/',views.saveDetails,name="saveDetails"),
       path('displayDetails/',views.displayDetails,name="displayDetails"),
       path('editDetails/<int:dataid>',views.editDetails,name="editDetails"),
       path('updateDetails/<int:dataid>',views.updateDetails,name="updateDetails"),
       path('deleteDetails/<int:dataid>',views.deleteDetails,name="deleteDetails"),
       path('loginpage/', views.loginpage, name="loginpage"),
       path('adminlogin/', views.adminlogin, name="adminlogin"),
       path('user_reg/', views.user_reg, name="user_reg"),
       path('userlogout/', views.userlogout, name="userlogout")

]