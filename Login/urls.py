from django.urls import path
from . import views

# urls for your app
urlpatterns = [
    # "REI" is our homepage
    path("", views.home, name="home"),

    # Adding path for "Shop"
    path("shop/", views.shop_view, name="shop"),

    # Adding path for "Cart"
    path("cart/", views.cart_view, name="cart"),

    # Path for "Login"
    path("login/", views.login_view, name="login"),
]
