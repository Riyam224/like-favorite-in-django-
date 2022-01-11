from django.urls import path
from .views import * 



urlpatterns = [
    path('' , index , name='index'),
    path('<int:id>' , product_detail , name='product_detail'),

    path('<int:id>/like_or_unlike' , like_or_unlike , name='like_or_unlike'),
    path('user_favorites' , user_favorites , name='user_favorites'),
]
