from django.urls import path, include

from shop_management import views

urlpatterns = [
    path('items/', views.GetPostItems.as_view()),
    path('items/<int:id>', views.GetPutDeleteItems.as_view()),
    path('owner/', views.GetPostOwner.as_view()),
    path('update_owner/', views.GetPutDeleteShopOwner.as_view()),
    path('buy_item/<str>', views.BuyItem.as_view()),
    path('sale_item/<str>', views.SaleItem.as_view())
]