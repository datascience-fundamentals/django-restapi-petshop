from functools import reduce
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from . import models
from datetime import datetime

"""
    <serialize-instance>.is_valid() -> Its required to invoke is_valid() when you
        send information in data property param of serializer class, becasue this class is prepared to valid
        all fields which are passed on data property, but not in the first param (model instance).
    <class-serializer>(<model-instance>,data=<payload_json>) -> If the constructor receive those two params.
        Then, the serializer validates the value sended on data property. After that, for any field provided
        in data property, the value from the payload will replace corresponding value in the instance. 
        Lastly, fields not included in data will retain their original value from the instance.
    <class-serializer>.data -> It contains the data serialized in format JSON friendly to send as JSON response
    <class-serializer>.validate_data -> It contains the data validated and deserialized. It's ideal for using in internal logic
"""


@api_view(["POST", "GET", "DELETE"])
def persons_crd(request):
    try:
        if "POST" == request.method:
            api_req = request.data
            person_serialize = serializers.PersonSerializer(data=api_req)
            if not person_serialize.is_valid():
                return Response(data=person_serialize.errors, status=status.HTTP_400_BAD_REQUEST)

            person_serialize.save()
            api_resp = {"msg": "Person created sucessfully",
                        "person": person_serialize.data}
            status_resp = status.HTTP_201_CREATED
        elif "GET" == request.method:
            persons = models.Person.objects.all()
            if not len(persons):
                api_resp = {"msg": "Persons empty"}
            else:
                persons_serialize = serializers.PersonSerializer(
                    persons, many=True)
                api_resp = {"msg": "Persons founded sucessfully",
                            "person": persons_serialize.data}
            status_resp = status.HTTP_200_OK
        elif "DELETE" == request.method:
            persons = models.Person.objects.all()
            persons.delete()
            api_resp = {"msg": "Persons deleted sucessfully"}
            status_resp = status.HTTP_204_NO_CONTENT

        return Response(data=api_resp, status=status_resp)

    except Exception:
        return Response(data={"msg": "Error at processing"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET", "PUT", "DELETE"])
def person_rud(request, pk):
    try:
        if "GET" == request.method:
            if models.Person.objects.filter(pk=pk).exists():
                person = models.Person.objects.get(pk=pk)
                person_serializer = serializers.PersonSerializer(person)
                api_resp = {"msg": "Person founded sucessfully",
                            "person": person_serializer.data}
            else:
                api_resp = {"msg": "Person doesn't exist"}
            status_resp = status.HTTP_200_OK
        elif "PUT" == request.method:
            if models.Person.objects.filter(pk=pk).exists():
                person = models.Person.objects.get(pk=pk)
                api_req = request.data

                person_serializer = serializers.PersonSerializer(
                    person, data=api_req)
                if not person_serializer.is_valid():
                    return Response(data=person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                person_serializer.save()
                api_resp = {"msg": "Person updated sucessfully"}
            else:
                api_resp = {"msg": "Person doesn't exist"}
            status_resp = status.HTTP_204_NO_CONTENT
        elif "DELETE" == request.method:
            if models.Person.objects.filter(pk=pk).exists():
                person = models.Person.objects.get(pk=pk)
                person.delete()
                api_resp = {"msg": "Person deleted sucessfully"}
            else:
                api_resp = {"msg": "Person doesn't exist"}

            status_resp = status.HTTP_204_NO_CONTENT
        return Response(data=api_resp, status=status_resp)
    except Exception:
        return Response(data={"msg": "Error at processing"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def adoption_hist(request):
    try:
        payload = {**request.query_params}
        api_req = [{f"{key}": value[0]} for key, value in payload.items() if key in [
            "start_date", "end_date"]]
        api_req = reduce(lambda acc, e: {**acc, **e}, api_req, {})

        adoption_hist_serialize = serializers.AdoptionHistSerializer(
            data=api_req)
        if not adoption_hist_serialize.is_valid():
            return Response(data=adoption_hist_serialize.errors, status=status.HTTP_400_BAD_REQUEST)

        start_date = adoption_hist_serialize.validated_data["start_date"]
        end_date = adoption_hist_serialize.validated_data["end_date"]

        adoptions = models.Adoption.objects.filter(
            adoption_date__gte=start_date, adoption_date__lte=end_date
        ).select_related("person", "pet", "pet__breed")

        adoption_hist_model_serializer = serializers.AdoptionHistModelSerializer(
            adoptions, many=True)
        return Response(data=adoption_hist_model_serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(data={"msg": "Error at processing"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


person_view = {
    "persons_crd": persons_crd,
    "person_rud": person_rud,
}

adoption_view = {
    "adoption_hist": adoption_hist,
}
