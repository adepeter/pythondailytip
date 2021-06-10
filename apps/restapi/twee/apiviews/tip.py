from rest_framework import generics

from ..serializers.tip import TipSerializer
from ....twee.models import PythonTip


class TipListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TipSerializer
    queryset = PythonTip.objects.all()


class TipRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TipSerializer
    queryset = PythonTip.objects.all()
    lookup_url_kwarg = 'id'
