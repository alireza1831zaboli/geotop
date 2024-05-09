from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import TemplateHTMLRenderer

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name="dispatch")
class Home2(APIView):
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        people = Person.objects.all()
        people_count = people.count()
        if people_count % 10 == 0:
            page_count = people_count // 10
        else:
            page_count = (people_count // 10) + 1

        page = 1
        if request.GET.get("page"):
            page = int(request.GET["page"])

        people = people[(page - 1) * 10 : page * 10]
        serializer = self.serializer_class(instance=people, many=True)

        return Response({"people": serializer.data, "page_count": page_count})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"people": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, person_id):
        try:
            print(person_id)
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response(
                {"error": "Person not found"}, status=status.HTTP_404_NOT_FOUND
            )

        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, person_id):
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response(
                {"error": "Person not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"people": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class Home(APIView):
    serializer_class = PersonSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "geotop.html"
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        people = Person.objects.all()
        people_count = people.count()
        if people_count % 10 == 0:
            page_count = people_count // 10
        else:
            page_count = (people_count // 10) + 1

        page = 1
        if request.GET.get("page"):
            page = int(request.GET["page"])

        people = people[(page - 1) * 10 : page * 10]
        serializer = self.serializer_class(instance=people, many=True)

        return Response({"people": serializer.data, "page_count": page_count})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"people": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, person_id):
        try:
            print(person_id)
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response(
                {"error": "Person not found"}, status=status.HTTP_404_NOT_FOUND
            )

        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EditPeople(APIView):
    serializer_class = PersonSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "geotop.html"

    def put(self, request, person_id):
        print("Koooooooooooooooon")
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response(
                {"error": "Person not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"people": serializer.data})

        print(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


