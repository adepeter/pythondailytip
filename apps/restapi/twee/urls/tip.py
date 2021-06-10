from django.urls import path, include

from ..apiviews.tip import TipListCreateAPIView, TipRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', TipListCreateAPIView.as_view(), name='list_create'),
    path('<int:id>/', include([
        path('', TipRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_update_destroy'),
    ]))
]
