
from django.contrib import admin
from django.urls import path
# from ..testapp import views
from testapp.views import test_email_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-email/', test_email_view),
]
