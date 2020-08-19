from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import date

from weather.utils import process_days_needs_umbrela


class CheckTakeUmbrelaFiveDaysView(APIView):

    def get(self, request, format=None):

        start_date = date.today()

        return Response(process_days_needs_umbrela(start_date, 5))
