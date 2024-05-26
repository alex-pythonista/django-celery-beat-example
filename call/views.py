import json
import datetime
import random
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django_celery_beat.models import ClockedSchedule, PeriodicTask


from .serializers import RestaurantSerializer



class EmailAPIView(GenericAPIView):
    serializer_class = RestaurantSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)

            scheduled_obj = ClockedSchedule.objects.create(
                clocked_time=datetime.datetime.now() + datetime.timedelta(minutes=2)
            )

            PeriodicTask.objects.create(
                name=f'test mail - try {random.randint(0, 1000)}',
                task="test_email",
                args=json.dumps([serializer.data['email']]),
                clocked=scheduled_obj,
                one_off=True
            )
            return Response(status=200)
        except Exception as e:
            return Response({
                'message': str(e),
            }, status=400)
        

class CallAPIView(GenericAPIView):
    serializer_class = RestaurantSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)

            scheduled_obj = ClockedSchedule.objects.create(
                clocked_time=datetime.datetime.now() + datetime.timedelta(minutes=2)
            )

            PeriodicTask.objects.create(
                name=f'test mail - try {random.randint(0, 1000)}',
                task="test_twilio_call",
                args=json.dumps([serializer.data['email']]),
                clocked=scheduled_obj,
                one_off=True
            )
            return Response(status=200)
        except Exception as e:
            return Response({
                'message': str(e),
            }, status=400)
