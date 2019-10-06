from django.urls import include, path

urlpatterns = [
    path('orenza/', include('orenza.urls')),
    path('gargantos/', include('gargantos.urls')),
]
