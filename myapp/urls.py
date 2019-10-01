from django.urls import path
from myapp import views
app_name='myapp'

urlpatterns=[
    path('page3/',views.page3,name="page3"),
]