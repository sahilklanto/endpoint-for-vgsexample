from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import SaveDataModelSerializer
from rest_framework import status
from api.models import SaveData
from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class DummyView(APIView):

    def post(self, request):
        query = SaveData.objects.create(entry='The 3rd Party view has done whatever it needs to after recieving the data')
        serialized_data = SaveDataModelSerializer(query)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
