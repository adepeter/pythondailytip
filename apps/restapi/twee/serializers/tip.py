from rest_framework import serializers

from ....twee.models import PythonTip


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonTip
        fields = '__all__'
        extra_kwargs = {
            'tip': {
                'max_length': 140
            }
        }
