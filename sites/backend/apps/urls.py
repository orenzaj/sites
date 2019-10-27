from django.urls import include, path

urlpatterns = [
    path('rhythm/', include('apps.rhythm.urls')),
]
