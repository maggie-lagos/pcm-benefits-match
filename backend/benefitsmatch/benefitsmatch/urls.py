"""
URL configuration for benefitsmatch project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include,path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from transactionlog.views import TransactionViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)

def health_check(request):
    return HttpResponse("OK")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token/', views.obtain_auth_token), # can subclass ObtainAuthToken for custom behavior
    path('api/', include((router.urls, 'transactions'), namespace='transactions')),
    path('health/', health_check, name='health_check'),
]
