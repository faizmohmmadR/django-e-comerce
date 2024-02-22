from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("",views.index,name='index'),
    path("product/list",views.product_list,name='product_list'),
    path("add/product/",views.add_product,name='add_product'),
    path("update/product/<int:pk>/",views.update_product,name="update_product"),
    path("product/detail/<int:pk>/",views.product_detail,name="product_detail"),
    path("delete/product/<int:pk>/",views.delete_product,name="delete_product"),
    path("customer/list/",views.customer_list,name='customer_list'),
    path("customer/list/",views.customer_list,name='customer_detail'),
    path("add/customer/",views.add_customer,name='add_customer'),
    path("update/customer/<int:pk>",views.update_customer,name="update_customer"),
    path("delete/customer/<int:pk>",views.delete_customer,name="delete_customer"),
    path("order/list/",views.order_list,name="order_list"),
    path("add/order/",views.add_order,name="add_order"),
    path("update/order/<int:pk>",views.update_order,name="update_order"),
    path("delete/order/<int:pk>",views.delete_order,name="delete_order"),
]