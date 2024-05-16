from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product' , views.Product_Viewset)
router.register('review' , views.Review_Viewset)

app_name = 'product'

urlpatterns = [

    path('product/<str:slug>/rate_product/' , views.Product_Viewset.as_view({'post':'rate_product'}) , name = 'rate_product')

]

urlpatterns += router.urls