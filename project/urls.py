from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('abc_app.urls')),
    # Redirect root '/' to '/list/' so the todo list is the landing page
    path('', RedirectView.as_view(url='/list/', permanent=False)),
]