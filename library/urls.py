from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'books', views.BookListView)
router.register(r'profiles', views.UserProfileView)
router.register(r'carts', views.CartView)
router.register(r'history', views.BookHistoryView)

urlpatterns = [
    #path('api/', include(router.urls)),
    path('', views.home ),
]
