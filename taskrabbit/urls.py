from django.contrib import admin
from django.urls import path
from regisAndAuth import views
from rest_framework import router

router = DefaultRouter()
router.register('regisAndAuth', views.UserModelViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include(router.urls)),
    path("auth/",include("rest_framework.urls",namespade="rest_framework")),
]
