from rest_framework.serializers import ModelSerializer
from api.models import SaveData


class SaveDataModelSerializer(ModelSerializer):

    class Meta:
        model = SaveData
        fields = '__all__'
