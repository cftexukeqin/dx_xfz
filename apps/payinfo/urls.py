from django.urls import path
from . import views
app_name = 'payinfo'
urlpatterns = [
    path('',views.payinfo,name='payinfo'),
    path('payinfo_order/',views.payinfo_order,name='payinfo_order'),
    path('notify_url/',views.notify_view,name='notify_url'),
    path('download/',views.down_file,name='download'),
]