from rest_framework.response import Response
from rest_framework.views import APIView


class CheckTakeUmbrelaFiveDaysView(APIView):

    def get(self, request, format=None):
        return Response("You should take an umbrella in these days:..")
