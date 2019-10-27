from django.urls import include, path

urlpatterns = [
    path('orenza/', include('sites.orenza.urls')),
    path('gargantos/', include('sites.gargantos.urls')),
]

