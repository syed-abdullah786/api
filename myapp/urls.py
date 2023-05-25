from django.urls import path

from . import views
from rest_framework_nested import routers
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register('items', views.ItemViewSet, basename="item"),

urlpatterns = [
                  # path('item/', views.CustomerViewSet.as_view())
                  # path('employees/', views.User.as_view()),
              ]+router.urls