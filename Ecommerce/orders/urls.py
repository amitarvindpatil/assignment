from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [

    path('products/', views.get_post_product.as_view(),
         name="get_post_product"),

    path('products/<pk>', views.get_delete_update_product.as_view(),
         name="get_delete_update_product"),

    path('orderitem/', views.get_post_orderitem.as_view(),
         name="get_post_orderitem"),

    path('orderitem/<pk>', views.get_delete_update_orderitems.as_view(),
        name="get_delete_update_orderitems"),

    path('orders/', views.get_post_order.as_view(),
         name="get_post_order"),

    path('orders/<pk>', views.get_delete_update_order.as_view(),
         name="get_delete_update_order"),

]
