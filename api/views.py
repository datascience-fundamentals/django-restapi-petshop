from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from . import models


@api_view(['POST'])
def create_person(request):
    try:
        person_req = request.data
        personSerialize = serializers.PersonSerializer(data=person_req)
        if not personSerialize.is_valid():
            return Response(data=personSerialize.errors, status=status.HTTP_400_BAD_REQUEST)

        personSerialize.save()
        person_resp = personSerialize.data
        return Response(data={"msg": "Person created sucessfully", "person": person_resp}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(data={"msg": "Error al crear persona"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


person_view = {
    "create_person": create_person
}
