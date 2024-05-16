from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category' , views.Category_Viewset)

app_name = 'category'

urlpatterns = [

    path('category/<str:category_slug>/filter_by_category/' , views.Category_Viewset.as_view({'get':'filter_by_category'}) , name = 'filter_by_category')

]

urlpatterns += router.urls
