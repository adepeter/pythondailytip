from django.urls import path, include

urlpatterns = [
    path('tip/', include('apps.restapi.twee.urls.tip'))
]
