from django.urls import path
from . import views

urlpatterns = [
    path('deposit_products/', views.deposit_products ),
    path('saving_products/', views.saving_products ),
    path('save_products/', views.save_products),
    path('deposit_products_options/<str:fin_prdt_cd>/', views.deposit_products_options ),
    path('saving_products_options/<str:fin_prdt_cd>/', views.saving_products_options ),
    # path('deposit_products/top_rate/', views.top_rate ),

]
