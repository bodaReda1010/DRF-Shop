from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [

    path('make_order/' , views.make_order , name = 'make_order'),
    path('place_order/' , views.place_order , name = 'place_order'),
    path('order_complete/' , views.order_complete , name = 'order_complete'),

]