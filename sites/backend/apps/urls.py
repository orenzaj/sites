from django.urls import include, path

urlpatterns = [
    path('rhythm/', include('apps.rhythm.urls'), name="rhythm"),
    path('chat/', include('apps.chat.urls'), name="chat"),
]
