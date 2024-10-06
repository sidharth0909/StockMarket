from django.contrib import admin
from django.urls import path
from valuations.views import valuation_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', valuation_view, name='valuation'),
]
