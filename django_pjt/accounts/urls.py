from django.urls import path
from . import views


urlpatterns = [
    # path('profile/', views.user_profile_detail),
    path('user/edit/', views.user_profile_edit),
    path('user/financial/', views.user_financial_edit),
    path('user/mbti/', views.user_mbti_edit),
    path('user/recommended_product/', views.product_mbti),
]
